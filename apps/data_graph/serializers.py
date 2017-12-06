from rest_framework import serializers

from apps.data_graph.models import GraphObject


class GraphObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphObject
        fields = ('id', 'name', 'title', 'user', 'fields',)