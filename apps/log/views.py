from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
# Create your views here.
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_bin.models import Bin
from apps.log.models import Log
from apps.log.serializers import LogSerializer


class UserBinLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Get list user search
    """
    # permission_classes = (PublicEndpoint,)
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    # serializer_class = LogSerializer
    # model = Log

    def list(self, request):
        user = self.request.user
        queryset = Log.objects.filter(user=user, event__startswith='/data-bin-loader/').order_by('-datetime')


        res = []
        for log in queryset:
            try:
                if 'jsonQuery' in log.query.keys():
                    jsonQuery = log.query['jsonQuery']
                    bin_id = log.event.split('/')[3]
                    if bin_id == 32:
                        print('test')
                    try:
                        bin_name = Bin.objects.get(pk=bin_id).name
                    except:
                        bin_name = ''


                    item = {
                        'event': log.event,
                        'bin_id': bin_id,
                        'bin_name': bin_name,
                        'jsonQuery': jsonQuery,
                        'datetime': log.datetime
                    }
                    res.append(item)
            except:
                print(log.query)

        # serializer = LogSerializer(queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(res, status=status.HTTP_200_OK)
