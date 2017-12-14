from rest_framework import views, status, generics
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.model_graph import Graph, GraphModel
from apps.data_graph.models.model_graph_data import GraphData, GraphNode
from apps.data_graph.serializers import GraphNodeSerializer


class ClearGraphNodeView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        name = self.kwargs['graph_name']
        user = self.request.user
        graph = Graph.objects.get(name=name)
        if user != graph.user:
            raise Exception( "You are not a graph's owner")
        deleted = GraphNode.objects.filter(graph=graph).delete()
        return Response([deleted], status=status.HTTP_200_OK)



class GraphNodeListView(generics.ListAPIView):
    """
    Return 'Bin' list for current user
    """
    serializer_class = GraphNodeSerializer
    #permission_classes = (IsAdminUser,)

    def get_queryset(self):
        name = self.kwargs['graph_name']
        user = self.request.user
        graph = Graph.objects.get(name=name)
        if user != graph.user:
            raise Exception( "You are not a graph's owner")
        queryset = GraphNode.objects.filter(graph=graph)
        return queryset


class GraphNodesByModelsView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        """
        Save to DB or Get in JSON nodes for models in Graph object
        :param request.data:
            json model names array, like: ["person", "phone"]
        :param args:
        :param kwargs:
            action - optional from ["save","get"]
            graph_name - name field of Graph object
        :return:
        """
        user = self.request.user
        graph_name = self.kwargs['graph_name']
        action = self.kwargs['action']
        model_names_json = request.data

        try:
            graph = Graph.objects.get(name=graph_name)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        synonym_models = [
            'phoneA','phoneB',
        ]

        arr_data = []
        #arr_data_pk = []
        arr_data_super_pk = []
        count = 0
        for model_name in model_names_json:
            model = GraphModel.objects.get(name=model_name)

            #syn_model_names = synonym_models[model_name]

            graph_data = GraphData.objects.filter(graph=graph, data__has_keys=model.fields)

            #check synonims data

            if len(graph_data)>0:
                for item in graph_data:
                    # define constraints super_pk
                    super_pk = ''
                    for key in model.fields:
                        super_pk += '__' + item.data[key]

                    if (False):
                    #if (super_pk in arr_data_super_pk) :
                        #TODO check synonym models

                        d=1

                    else:
                        if ('save'.__eq__(action)):
                            graph_node = GraphNode(graph=graph,
                                                   model=model,
                                                   graph_data=item)
                            graph_node.save()
                            count += 1
                        elif ('get'.__eq__(action)):
                            #item.data['group'] = model_name
                            item.data['label'] = super_pk

                            item.data['shape'] = 'circularImage'
                            item.data['image'] = 'http://localhost:8000/static/django.jpg'

                            item.data['super_pk'] = super_pk
                            arr_data.append(item.data)
                            #arr_data_pk.append(item.pk)
                        arr_data_super_pk.append(super_pk)


        if ('save'.__eq__(action)):
            return Response([count], status=status.HTTP_200_OK)
        elif ('get'.__eq__(action)):
            return Response(arr_data, status=status.HTTP_200_OK)
        else:
            raise Exception("Action not found, check URL, it should be one of ['save','get']")
