from rest_framework import serializers

from apps.data_graph.models import GraphObject, GraphObjectDrawing


class GraphObjectDrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphObjectDrawing
        fields = ('id', 'json',)


class GraphObjectSerializer(serializers.ModelSerializer):
    drawing = GraphObjectDrawingSerializer()

    class Meta:
        model = GraphObject
        fields = ('id', 'name', 'title', 'user', 'fields', 'drawing',)


