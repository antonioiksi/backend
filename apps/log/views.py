from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.log.models import Log
from apps.log.serializers import LogSerializer


class UserBinLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = LogSerializer
    model = Log

    def list(self, request):
        user = self.request.user
        queryset = Log.objects.filter(user=user)
        serializer = LogSerializer(queryset, many=True)
        return Response(serializer.data)
