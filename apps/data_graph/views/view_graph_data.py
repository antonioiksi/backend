from rest_framework import viewsets, views, status
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models import GraphData, GraphObject


class ClearUserGraphDataView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        deleted = GraphData.objects.filter(user=user).delete()
        return Response([deleted], status=status.HTTP_200_OK)


class LoadGraphDataView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        user = self.request.user

        count = 0
        for item in request.data:
            graphData = GraphData(data=item, user=user)
            graphData.save()
            count+=1

        return Response([count], status=status.HTTP_200_OK)


class GraphDataByObjectNameView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        object_name = self.kwargs['object_name']

        try:
            object = GraphObject.objects.get(name=object_name)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        objects = GraphData.objects.filter(data__has_keys=object.fields)
        arr_data = []
        if len(objects)>0:
            arr_data = [item.data for item in objects]

        for el in arr_data:
            el['group'] = object_name

        return Response(arr_data, status=status.HTTP_200_OK)