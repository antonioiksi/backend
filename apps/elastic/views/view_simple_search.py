import json

import requests
from rest_framework import views, status
from rest_framework.response import Response

from backend import settings

from apps.log.mixins import RequestLogViewMixin


class SimpleSearchView(RequestLogViewMixin, views.APIView):
    """
    Make search according official ElasticSearch docs.
    In fact it transports json to ES and return result filtering by 'hits' node in json
    request.data:
    json request must comply with ElasticSearch rules (https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
    """
    #permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        #serializer = QuerySerializer(data=request.data)
        #serializer.is_valid()
        #js = serializer.validated_data
        # TODO add checking input param http://json-schema.org/

        r = requests.post(settings.ELASTIC_SEARCH_URL+"/_search", json.dumps(request.data))
        data = r.json()
        #source_arr = [x['_source'] for x in data['hits']['hits']]
        if r.status_code == 200:
            return Response( data['hits'], status=status.HTTP_200_OK)
        else:
            return Response('app_elastic error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #raise APIException("There was a problem!")