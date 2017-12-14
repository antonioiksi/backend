from pprint import pprint

from rest_framework import views, status
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import Graph, GraphModel, GraphRelation
from apps.data_graph.models.model_graph_data import GraphData, GraphNode


class GraphEdgesByRelationsView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        """
        Get edges for
        :param request.data:
            json - array of Relation object's names, like:
            ["call_to", "same_index_type",]
        :param args:
        :param kwargs:
            graph_name - name field of Graph object
        :return:
            json array with edges like [{from: 324, to: 211},...] 344 and 211 pk from GraphNode
        """
        user = self.request.user
        graph_name = self.kwargs['graph_name']
        relation_names_json = request.data

        try:
            graph = Graph.objects.get(name=graph_name)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        arr_data = []
        for relation_name in relation_names_json:
            relation = GraphRelation.objects.get(name=relation_name)

            graph_data1 = GraphNode.objects.filter(graph_data__data__has_keys=relation.from_fields)
            for it in graph_data1:
                pprint(it.graph_data.data)

            graph_data2 = GraphNode.objects.filter(graph_data__data__has_keys=relation.to_fields)
            for it in graph_data2:
                pprint(it.graph_data.data)


            #graph_data1 = GraphData.objects.filter(data__has_keys=relation.from_fields)
            #graph_data2 = GraphData.objects.filter(data__has_keys=relation.to_fields)




            for item2 in graph_data2:
                for item1 in graph_data1:
                    if (item1.pk!=item2.pk):
                        success = True
                        for i in range(len(relation.from_fields)):
                            value1 = item1.graph_data.data[relation.to_fields[i]]
                            value2 = item2.graph_data.data[relation.from_fields[i]]
                            if (value1!=value2):
                                success = False
                                break
                        if(success):
                            edge = {
                                'from': item1.pk,
                                'to': item2.pk,
                                'name': relation_name
                            }
                            arr_data.append(edge)

        return Response(arr_data, status=status.HTTP_200_OK)