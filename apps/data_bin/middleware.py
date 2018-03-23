import datetime
import json
import socket
import time
from pprint import pprint

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from .models import Bin, BinItem


def get_user_jwt(request):
    """
    Replacement for django session auth get_user & auth.get_user
     JSON Web Token authentication. Inspects the token for the user_id,
     attempts to get that user from the DB & assigns the user on the
     request object. Otherwise it defaults to AnonymousUser.

    This will work with existing decorators like LoginRequired  ;)

    Returns: instance of user object or AnonymousUser object
    """
    user = None
    try:
        user_jwt = JWTTokenUserAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            token_user = user_jwt[0]
            user_id = token_user.pk
            user = User.objects.get(id=user_id)
    except:
        pass
    return user


class ElasticBinItemMiddleware(object):

    def process_request(self, request):
        user = get_user_jwt(request)
        request.user = user

        request.start_time = time.time()


    def process_response(self, request, response):

        if request.method != 'POST' or 'data' not in response.data:
            return response

        #request.user
        user = request.user

        user_id = request.user.pk
        user = None
        if user_id is not None:
            user = User.objects.get(id=user_id)
        #response.data
        try:
            bin = Bin.objects.get(active=True, user=user)
        except ObjectDoesNotExist:
            try:
                bin = Bin.objects.get(name='default', user=user)
                Bin.objects.filter(user=user).update(active=False)
                bin.active = True
                bin.save()
            except ObjectDoesNotExist:
                bin = Bin(user=user,
                          name='default',
                          active=True)


        #Bin.objects.filter(name='default',user=user.pk)

        jsonData = response.data
        data = jsonData['data']
        mapping = None
        if 'mapping' in response.data:
            mapping = jsonData['mapping']

        query = json.loads(request.body.decode("utf-8"))
        url = request.path_info
        #pprint(data)
        item = BinItem(bin=bin, data=data, mapping=mapping, query=query, url=url)
        item.save()

        return response
