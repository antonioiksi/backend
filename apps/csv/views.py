from rest_framework import views, status
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.log.mixins import RequestLogViewMixin


class CsvLoadView(RequestLogViewMixin, views.APIView):
    """



    """
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        _source1 = {'phone': '322223322', 'patronomic_name': 'ssp'}
        _source11 = {'phone': ['322223322']}
        _source2 = {'person_name': 'Petrov', 'musor': 'value musor'}
        _source22 = {'person_name': ['Petrov']}

        result = {'data': [
                            {
                                '_id': 1,
                                '_source': _source1,
                                '_data_system_source': _source11},
                            {
                                '_id': 2,
                                '_source': _source2,
                                '_data_system_source': _source22},
                            ],
                  'mapping_type': 0}

        return Response(result, status=status.HTTP_200_OK)
