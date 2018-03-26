from django.shortcuts import render
# Create your views here.
from rest_framework import generics, renderers

from apps.auth_jwt.permissions import PublicEndpoint

from .models import Attribute, EntityAttribute
from .serializers import (AttributeSerializer, EntityAttributeSerializer,
                          EntityAttributeSimpleSerializer)


class AttributeListView(generics.ListAPIView):
    """
    Get list of attribute (attribute is the same as field name)
    """
    permission_classes = (PublicEndpoint,)
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()


class EntityAttributeListView(generics.ListAPIView):
    """
    Get list of search attribute
    """
    permission_classes = (PublicEndpoint,)
    serializer_class = EntityAttributeSerializer
    queryset = EntityAttribute.objects.all()


class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        result = {}
        for item in data:
            result['name'] = item['name']
            result['title'] = item['title']
            attr_list = item['attributes']
            attr_list2 = []
            for attr in attr_list:
                attr_list2.append(attr['name'])
            result['attributes'] = attr_list2

        data = result
        return super(CustomRenderer, self).render(data, accepted_media_type, renderer_context)


class EntityAttributeCustomListView(generics.ListAPIView):
    """
    Get list of search attribute
    """
    # permission_classes = (PublicEndpoint,)
    serializer_class = EntityAttributeSerializer
    queryset = EntityAttribute.objects.all()
    renderer_classes = (CustomRenderer, renderers.BrowsableAPIRenderer)


class MappingRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        result = {}
        for item in data:
            search_attr_name = item['name']
            # result['title'] = item['title']
            attr_list = item['attributes']
            attr_list2 = []
            for attr in attr_list:
                attr_list2.append(attr['name'])
            result[search_attr_name] = attr_list2

        data = result
        return super(MappingRenderer, self).render(data, accepted_media_type, renderer_context)


class EntityAttributeMappingListView(generics.ListAPIView):
    """
    Get list of search attribute
    """
    # permission_classes = (PublicEndpoint,)
    serializer_class = EntityAttributeSerializer
    queryset = EntityAttribute.objects.all()
    renderer_classes = (MappingRenderer, renderers.BrowsableAPIRenderer)
