from rest_framework import views, status, viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphModelDrawing
from apps.data_graph.serializers import GraphModelDrawingSerializer


class GraphModelDrawingViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request):
        user = self.request.user
        queryset = GraphModelDrawing.objects.all()
        serializer = GraphModelDrawingSerializer(queryset, many=True)
        return Response(serializer.data)

