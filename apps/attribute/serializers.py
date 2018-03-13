from rest_framework import serializers

from .models import Attribute, EntityAttribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name', 'title',)


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name',)


class EntityAttributeSerializer(serializers.ModelSerializer):
    attributes = AttributeNameSerializer(many=True, read_only=True)

    class Meta:
        model = EntityAttribute
        fields = ('name', 'title', 'attributes',)


class EntityAttributeSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntityAttribute
        fields = ('name', 'title',)
