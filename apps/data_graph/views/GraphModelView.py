from rest_framework import viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphModel
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
        pass

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
