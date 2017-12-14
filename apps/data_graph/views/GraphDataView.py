from rest_framework import viewsets, views, status
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphModel, Graph
from apps.data_graph.models.model_graph_data import GraphData


class ClearGraphDataView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        user = self.request.user
        graph = Graph.objects.get(name=name)
        if user != graph.user:
            raise Exception( "You are not a graph's owner")
        deleted = GraphData.objects.filter(graph=graph).delete()
        return Response([deleted], status=status.HTTP_200_OK)


class LoadGraphDataView(views.APIView):
    """
    Post data into graph data with name = graph_data
    """
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        graph_name = self.kwargs['graph_name']
        user = self.request.user
        graph = Graph.objects.get(name=graph_name)

        count = 0
        for item in request.data:
            graphData = GraphData(data=item, graph=graph)
            graphData.save()
            count+=1
        return Response([count], status=status.HTTP_200_OK)


class GraphDataByModelNameView(views.APIView):
    """
    get graph data by model name
    """
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        model_name = self.kwargs['model_name']
        try:
            model = GraphModel.objects.get(name=model_name)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        objects = GraphData.objects.filter(data__has_keys=model.fields)
        arr_data = []
        if len(objects)>0:
            arr_data = [item.data for item in objects]

        for el in arr_data:
            el['group'] = model_name

        return Response(arr_data, status=status.HTTP_200_OK)


class JsonbFilterView(views.APIView):
    '''
    https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/fields/

    '''
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        #pk = self.kwargs['pk']

        arr = GraphData.objects.all()
        #GraphData.objects.filter(data__contains='"_index":"shakespeare"')
        arr1 = GraphData.objects.filter(data__contains={'_id': '40001'})

        GraphData.objects.filter(data__has_keys=['_id', '_index'])

        arr_data = [ item.data for item in arr1]

        return Response(arr_data, status=status.HTTP_200_OK)