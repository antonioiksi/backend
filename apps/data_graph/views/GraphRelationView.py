from rest_framework import views, status, viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphRelation, Graph
from apps.data_graph.serializers import GraphRelationSerializer


class GraphRelationViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request):
        queryset = GraphRelation.objects.all()
        serializer = GraphRelationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = self.request.user
        serializer = GraphRelationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        graph_pk = serializer.initial_data['graph']
        graph = Graph.objects.get(pk=graph_pk)
        queryset = GraphRelation.objects.filter(graph=graph)
        serializer = GraphRelationSerializer(queryset, many=True)
        return Response(serializer.data)