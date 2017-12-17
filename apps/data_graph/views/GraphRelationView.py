from rest_framework import views, status, viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import GraphRelation, Graph
from apps.data_graph.models.model_graph_data import GraphNode, GraphNodeEdge
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


class GraphRelationBuilderView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        name = self.kwargs['graph_name']
        user = self.request.user
        graph = Graph.objects.get(name=name)
        if user != graph.user:
            raise Exception( "You are not a graph's owner")

        nodes = GraphNode.objects.filter(graph=graph)

        counter = {

        }

        for relation_name in request.data:
            relation = GraphRelation.objects.get(name=relation_name)

            count = 0

            for i1 in range(len(nodes)):
                for i2 in range(i1+1, len(nodes)):
                    node1 = nodes.get(i1)
                    node2 = nodes[i2]
                    if (node1.id != node2.id):
                        success = True
                        for i in range(len(relation.from_fields)) :
                            val1 = node1[relation.from_fields[i]]
                            val2 = node2[relation.from_fields[i]]
                            if (val1!=val2):
                                success = False
                                break
                        if (success):
                            edge = GraphNodeEdge(
                                relation=relation,
                                from_node=node1,
                                to_node=node2,
                            )
                            edge.save()
                            count += 1
                    counter[relation_name] = count

        return Response(counter, status=status.HTTP_200_OK)
