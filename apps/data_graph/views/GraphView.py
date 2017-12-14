from rest_framework import views, status, viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import Graph, GraphModel
from apps.data_graph.serializers import GraphSerializer


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


class GraphActivateView(views.APIView):

    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        user = self.request.user

        graph = Graph.objects.get(name=name, user=user)
        Graph.objects.filter(user=user).update(active=False)
        graph.active = True
        graph.save()

        list = [GraphSerializer(bin).data for bin in Graph.objects.filter(user=user)]
        #serializer = BinSerializer(bin)
        #return Response(json.dumps( serializer.data, ensure_ascii=False), status=status.HTTP_200_OK)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(list, status=status.HTTP_200_OK)