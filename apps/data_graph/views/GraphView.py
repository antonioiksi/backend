from rest_framework import views, status, viewsets
from rest_framework.response import Response
from apps.auth_jwt.permissions import PublicEndpoint

from apps.data_graph.models.Graph import Graph
from apps.data_graph.serializers.GraphSerializer import GraphSerializer


class GraphViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request):
        user = self.request.user
        queryset = Graph.objects.filter(user=user)
        serializer = GraphSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = self.request.user
        serializer = GraphSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        #serializer.save()
        queryset = Graph.objects.filter(user=user)
        serializer = GraphSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = self.request.user
        graph = Graph.objects.get(pk=pk)
        if(user!=graph.user):
            raise Exception("Yuo are not a graph owner")
        serializer = GraphSerializer(graph)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        user = self.request.user
        Graph.objects.get(pk=pk).delete()
        queryset = Graph.objects.filter(user=user)
        serializer = GraphSerializer(queryset, many=True)
        return Response(serializer.data)