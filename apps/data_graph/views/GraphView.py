from rest_framework import views, status, viewsets
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory, force_authenticate

from apps.auth_jwt.permissions import PublicEndpoint

from apps.data_graph.models.Graph import Graph
from apps.data_graph.serializers.GraphSerializer import GraphSerializer
from apps.data_graph.views.GraphModelView import CopyGraphModelsFromTemplatesView
from apps.data_graph.views.GraphRelationView import CopyGraphRelationsFromTemplatesView


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
        graph_id = str(serializer.data['id'])
        # print(serializer.data['id'])
        # serializer.save()

        try:
            # create init models for graph '/graph/model/copy-templates/{graph_id}'
            factory = APIRequestFactory()
            req = factory.get('/graph/model/copy-templates/' + graph_id)
            force_authenticate(req, user=user)
            view = CopyGraphModelsFromTemplatesView.as_view()
            res = view(req, graph_id=graph_id)
        except:
            print('models copying failed')

        try:
            # create init relations for graph '/graph/relation/copy-templates/{graph_id}'
            factory = APIRequestFactory()
            req = factory.get('/graph/relation/copy-templates/' + graph_id)
            force_authenticate(req, user=user)
            view = CopyGraphRelationsFromTemplatesView.as_view()
            res = view(req, graph_id=graph_id)
        except:
            print('relation copying failed')

        queryset = Graph.objects.filter(user=user)
        serializer = GraphSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = self.request.user
        graph = Graph.objects.get(pk=pk)
        if (user != graph.user):
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
