import json

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.test import RequestsClient, APIRequestFactory

from apps.attribute.models import Attribute
from apps.attribute.serializers import AttributeSerializer
from apps.auth_jwt.permissions import PublicEndpoint
from apps.elastic.views.view_mapped_field_list import MappedFieldListView
from apps.log.mixins import RequestLogViewMixin
import requests

from backend import settings


class AddedMappedFieldListView(RequestLogViewMixin, views.APIView):
    """

    """

    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):

        try:
            request = APIRequestFactory().get('/elastic/mapped-field-list/')
            response = MappedFieldListView.as_view()(request).render()
            response_json = json.loads(response.content.decode('utf8'))

            # output_dict = [x for x in data if x['type'] == '1']
            # values_arr = [x['_source']['play_name'] for x in data['hits']['hits']]
            # pprint(values_arr)
        except Exception as e:
            return Response('app_elastic error: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Attribute.objects.all().delete()
        found = 0
        added = 0
        for key in response_json.keys():
            # print('key'+key)
            found += 1
            if not Attribute.objects.filter(name=key):
                Attribute(title=key, name=key).save()
                added += 1

        return Response({'found': found, 'added': added, }, status=status.HTTP_200_OK)
