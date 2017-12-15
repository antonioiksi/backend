from rest_framework import viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphModel, Graph
from apps.data_graph.serializers import GraphModelSerializer



class GraphModelViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request):
        #user = self.request.user
        #queryset = GraphModel.objects.filter(user=user)
        queryset = GraphModel.objects.all()
        serializer = GraphModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = self.request.user
        serializer = GraphModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        graph_pk = serializer.initial_data['graph']
        graph = Graph.objects.get(pk=graph_pk)
        queryset = GraphModel.objects.filter(graph=graph)
        serializer = GraphModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = self.request.user
        graph_model = GraphModel.objects.get(pk=pk)
        #graph_model = get_object_or_404(queryset, pk=pk)
        serializer = GraphModelSerializer(graph_model)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


#class GraphModelViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = GraphModel.objects.all()
#    serializer_class = GraphModelSerializer