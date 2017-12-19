from rest_framework import serializers

from apps.data_graph.models.GraphModel import GraphModel


class GraphModelSerializer(serializers.ModelSerializer):
    #graph = GraphSerializer()
    #drawing = GraphModelDrawingSerializer()

    class Meta:
        model = GraphModel
        fields = ('id', 'name', 'graph', 'fields', 'is_group', 'drawing',)


class GraphModelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphModel
        fields = ('name',)
