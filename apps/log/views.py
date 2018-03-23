from django.shortcuts import render
# Create your views here.
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.log.models import Log
from apps.log.serializers import LogSerializer


class UserBinLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Get list user search
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = LogSerializer
    model = Log

    def list(self, request):
        user = self.request.user
        queryset = Log.objects.filter(user=user, event='/elastic-bin/mapped-search/').order_by('datetime')
        serializer = LogSerializer(queryset, many=True)
        return Response(serializer.data)
