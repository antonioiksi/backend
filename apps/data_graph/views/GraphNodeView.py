import json
from rest_framework import views, status, generics
from rest_framework.response import Response
from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models.Graph import Graph
from apps.data_graph.models.GraphData import GraphData
from apps.data_graph.models.GraphModel import GraphModel
from apps.data_graph.models.GraphModelDrawing import GraphModelDrawing
from apps.data_graph.models.GraphNode import GraphNode
from apps.data_graph.serializers.GraphNodeSerializer import GraphNodeSerializer, GraphNodeJsonSerializer
from copy import deepcopy

class GraphNodeClearView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        graph_id = self.kwargs['graph_id']
        user = self.request.user
        graph = Graph.objects.get(pk=graph_id)
        if user != graph.user:
            raise Exception( "You are not a graph's owner")
        deleted = GraphNode.objects.filter(graph=graph).delete()
        return Response([deleted], status=status.HTTP_200_OK)


class GraphNodeListView(views.APIView):
    """
    Return 'Bin' list for current user
    """
    serializer_class = GraphNodeJsonSerializer # GraphNodeSerializer
    #permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        graph_id = self.kwargs['graph_id']
        user = self.request.user
        graph = Graph.objects.get(pk=graph_id)
        if user != graph.user:
            raise Exception( "You are not a graph's owner")
        #queryset = GraphNode.objects.filter(graph=graph)
        array = GraphNode.objects.values_list('node_json', flat=True)
        #return queryset

        return Response(array, status=status.HTTP_200_OK)


class GraphNodeAddForModelsView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        """
        Save to DB JSON nodes for models in Graph object
        :param request.data:
            json model names array, like: ["person", "phone"]
        :param args:
        :param kwargs:
            action - optional from ["save","get"]
            graph_name - name field of Graph object
        :return:
        """
        user = self.request.user
        graph_id = self.kwargs['graph_id']
        #action = self.kwargs['action']
        model_names_json = request.data

        try:
            graph = Graph.objects.get(pk=graph_id)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        #arr_data = []
        arr_node_pk = []
        arr_graph_node_pk = []
        #arr_data_super_pk = []
        count = 0
        res = []
        for model_name in model_names_json:
            model = GraphModel.objects.get(graph=graph, name=model_name)

            graph_data = GraphData.objects.filter(graph=graph, data__has_keys=model.fields)

            if len(graph_data)>0:
                for item in graph_data:

                    # Get node_pk from model.fields
                    node_pk = ''
                    for key in model.fields:
                        node_pk += '__' + item.data[key]

                    if node_pk in arr_node_pk:
                        break

                    # make copy of json
                    item_json = json.dumps(item.data, default=lambda x: x.__dict__)

                    copied_item = json.loads(item_json) # deepcopy(item)

                    # TODO check if json data already has attr 'id' then rename it to '___old_id'
                    copied_item['id'] = node_pk
                    copied_item['label'] = copied_item[model.fields[0]]

                    if(model.is_group):
                        copied_item['group'] = model_name
                    else:
                        # TODO

                        for key in model.drawing.json:
                            if key=='image_field':
                                if not 'http' in copied_item[model.drawing.json['image_field']]:
                                    copied_item['image'] = 'http://localhost:8000/static'+copied_item[model.drawing.json['image_field']]
                                else:
                                    copied_item['image'] = copied_item[model.drawing.json['image_field']]
                                copied_item['brokenImage'] = 'http://localhost:8000/static/django.jpg'
                                #https: // www.igroved.ru / games / bondibon / busy - bugs /
                            else:
                                copied_item[key] = model.drawing.json[key]



                    graph_node = GraphNode(graph=graph,
                                               node_json=copied_item)
                    graph_node.save()
                    arr_node_pk.append(node_pk)

                    #graph_node.node_json["id"] = str(graph_node.pk)
                    #graph_node.save()

                    arr_graph_node_pk.append(graph_node.pk)
                    #GraphNode.objects.update()get(pk=pk)
                    # item.data['group'] = model_name
                    # item.data['label'] = super_pk
                    # item.data['shape'] = 'circularImage'
                    # item.data['image'] = 'http://localhost:8000/static/django.jpg'

                    # item.data['super_pk'] = super_pk
                    # arr_data.append(item.data)
                    # arr_data_pk.append(item.pk)
                    # arr_data_super_pk.append(super_pk)
                arr = GraphNode.objects.filter(pk__in=arr_graph_node_pk)
                res = [el.node_json for el in arr]

        return Response(res, status=status.HTTP_200_OK)
