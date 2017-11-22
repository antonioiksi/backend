from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.auth_jwt.permissions import PublicEndpoint
from .models import Attribute
from .serializers import AttributeSerializer


class AttributeListView(generics.ListAPIView):
    """
    Возвращаем список разрешенных атрубутов для поиска
    """
    permission_classes = (PublicEndpoint,)
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()

