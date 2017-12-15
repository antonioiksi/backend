from rest_framework import serializers

from apps.data_graph.models.model_graph import GraphModelDrawing, Graph, GraphModel, GraphRelation
from apps.data_graph.models.model_graph_data import GraphNode, GraphData


class GraphSerializer(serializers.ModelSerializer):
    graphdata_count = serializers.IntegerField(
        source='graphdata_set.count',
        read_only=True
    )
    class Meta:
        model = Graph
        fields = ('id', 'name', 'user', 'active', 'graphdata_count')


class GraphModelDrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphModelDrawing
        fields = ('id', 'name', 'json',)


class GraphModelSerializer(serializers.ModelSerializer):
    #graph = GraphSerializer()
    #drawing = GraphModelDrawingSerializer()

    class Meta:
        model = GraphModel
        fields = ('id', 'name', 'graph', 'fields', 'drawing',)

class GraphModelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphModel
        fields = ('name',)


class GraphRelationSerializer(serializers.ModelSerializer):
    #graph = GraphSerializer()

    class Meta:
        model = GraphRelation
        fields = ('id', 'name', 'graph', 'from_fields', 'to_fields',)


class GraphDataSerializer(serializers.ModelSerializer):
    #graph = GraphSerializer()

    class Meta:
        model = GraphData
        fields = ('id', 'data',)



class GraphNodeSerializer(serializers.ModelSerializer):
    #model = GraphModelSerializer()
    model = GraphModelNameSerializer()
    graph_data = GraphDataSerializer()

    class Meta:
        model = GraphNode
        fields = ('id', 'model', 'graph_data',)
