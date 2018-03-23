from rest_framework import status, views, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.Graph import Graph
from apps.data_graph.models.GraphModel import GraphModel
from apps.data_graph.models.ModelTemplate import ModelTemplate
from apps.data_graph.serializers.GraphModelSerializer import \
    GraphModelSerializer


class GraphModelForGraphViewSet(ListAPIView):
    permission_classes = (PublicEndpoint,)

    serializer_class = GraphModelSerializer
    def get_queryset(self):
        graph_id = self.kwargs['graph_id']
        #user = self.request.user
        graph = Graph.objects.get(pk=graph_id)
        queryset = GraphModel.objects.filter(graph=graph)
        #queryset = GraphModel.objects.all()
        return queryset


class GraphModelViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request, *args, **kwargs):
        #graph_id = self.kwargs['graph_id']
        #user = self.request.user
        #graph = Graph.objects.get(pk=graph_id)
        #queryset = GraphModel.objects.filter(graph=graph)
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


class CopyGraphModelsFromTemplatesView(views.APIView):
    # adding models for graph from user's ModelTemplates
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        graph_id = self.kwargs['graph_id']
        graph = Graph.objects.get(pk=graph_id)

        count = 0
        countErr = 0
        userModelTemplates = ModelTemplate.objects.filter(user=user)
        for userModelTemplate in userModelTemplates:
            graphModels = GraphModel.objects.filter(graph=graph, name=userModelTemplate.name)
            if len(graphModels) == 0:
                graphModel = GraphModel(
                    graph=graph,
                    name=userModelTemplate.name,
                    fields=userModelTemplate.fields[:],
                    is_group=userModelTemplate.is_group,
                    drawing=userModelTemplate.drawing
                )
                graphModel.save()
                count += 1

        return Response({'Created': count, 'Error': countErr}, status=status.HTTP_200_OK)
