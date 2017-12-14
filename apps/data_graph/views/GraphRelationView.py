from rest_framework import views, status, viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphRelation
from apps.data_graph.serializers import GraphSerializer, GraphRelationSerializer


class GraphRelationViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request):
        queryset = GraphRelation.objects.all()
        serializer = GraphRelationSerializer(queryset, many=True)
        return Response(serializer.data)
