import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from backend import settings


class TestDRFView(views.APIView):
    """

    """
    permission_classes = (PublicEndpoint,)

    def get(self, request):
        count = 1
        while (count < 999):
            print('The count is:', count)
            count = count + 1
        return Response(['ok'])


class TestDRFPostgresView(views.APIView):
    """

    """
    permission_classes = (PublicEndpoint,)

    def get(self, request):
        count = 1
        while (count < 999):
            print('The count is:', count)
            count = count + 1
        return Response(['ok'])


class TestDRFESView(views.APIView):
    """

    """
    permission_classes = (PublicEndpoint,)

    def get(self, request):
        count = 1
        while (count < 999):
            print('The count is:', count)
            count = count + 1

        try:
            es_search = requests.get(settings.ELASTIC_SEARCH_URL + "/_aliases")
            alias_list_json = es_search.json()
        except Exception as e:
            return Response('app_elastic error: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(alias_list_json)