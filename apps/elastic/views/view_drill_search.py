import json
from pprint import pprint

import requests
from rest_framework import status, views
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_bin.utils import add_value, get_new_value
from apps.log.mixins import RequestLogViewMixin
from backend import settings

input_json = """
{

    "deep": "3",
    "style": "strong",
    [
        {
            "phone": "2345233425",
            "name": "name 1"
        },
        {
            "type": "234534534",
        }
    ]
}"""

input_query = """{'query': {'bool': {'should': [{'match': {'speaker': 'king'}},
                               {'match': {'play_name': 'Henry'}}]}}}"""

query_match_all = """
{
    "query": {
        "match_all": {}
    }
}"""




class DrillSearchView(RequestLogViewMixin, views.APIView):
    """



    """
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        # TODO add checking input param http://json-schema.org/

        # sif
        if 'esQuery' in request.data:
            esQuery = request.data['esQuery']
        else:
            esQuery = request.data

        try:
            es_search = requests.post(
                settings.ELASTIC_SEARCH_URL + "/_search?size=" + settings.ELASTIC_SEARCH_RESULT_NUMBER,
                json.dumps(esQuery))
            # es_search = requests.get(settings.ELASTIC_SEARCH_URL + "/_search")
            search = es_search.json()
            # output_dict = [x for x in data if x['type'] == '1']
            # values_arr = [x['_source']['play_name'] for x in data['hits']['hits']]
            # pprint(values_arr)
        except Exception as e:
            return Response('app_elastic error: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Getting mapping
        mappings_res = {}
        hits_arr = search['hits']['hits']
        for hit in hits_arr:
            index_name = hit['_index']
            if index_name not in mappings_res:

                try:
                    es_mapping = requests.get(settings.ELASTIC_SEARCH_URL + '/' + index_name + '/_mapping')
                    mapping = es_mapping.json()
                except Exception as e:
                    return Response('app_elastic error getting mapping: %s' % e,
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                mapping = mapping[index_name]['mappings']

                tables_res = {}
                for table_name in mapping:
                    table_mapping = mapping[table_name]
                    # d = mapping[index_name]['mappings']['act']['properties']
                    # tables_mapping = [mapping[key] for key in mapping]
                    temp_dict = table_mapping['properties']

                    field_arr = {key: temp_dict[key] for key in temp_dict if temp_dict[key].get('fields') is not None}

                    tables_res[table_name] = field_arr

                mappings_res[index_name] = tables_res
                # TODO проход по JSON элементам а не по массиву
                # [d[key] for key in d if d[key]['type']=='text']
                # d = mapping['shakespeare']['mappings']['act']['properties']
                # [d[key] for key in d if d[key].get('fields') is None]

            # es_mapping = requests.get(settings.ELASTIC_SEARCH_URL + "shakespeare?pretty")
            # mapping = es_mapping.json()


        #result['mapping'] = mappings_res
        data = search['hits']['hits']

        # enrich data to datasystem attributes
        for data_item in data:
            _index = data_item['_index']
            _type = data_item['_type']
            _source = data_item['_source']
            _new_source = {}
            for _field, _value in _source.items():

                if _field in mappings_res[_index][_type].keys():
                    fields_dict = mappings_res[_index][_type][_field]['fields']
                    for f in fields_dict:

                        if f not in _new_source.keys():
                            # _new_source[f] = [get_new_value(_source, _field, _value)]
                            _new_source[f] = [_source[_field]]
                        else:
                            # _new_source[f].append(get_new_value(_source, _field, _value))
                            _new_source[f].append(_source[_field])

                # else:
                    # _new_source[_field] = _value

            data_item['_data_system_source'] = _new_source

        result = {}
        # source_arr = [x['_source'] for x in search['hits']['hits']]
        result['data'] = data
        result['mapping_type'] = 1    # PK for ElasticSearch 5.6


        return Response(result, status=status.HTTP_200_OK)
