from rest_framework import serializers

from .models import Attribute, EntityAttribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name', 'title',)

#
# class AttributeNameSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Attribute
#        fields = ('name',)
###

class EntityAttributeSerializer(serializers.ModelSerializer):
    # attributes = AttributeNameSerializer(many=True, read_only=True)
    attr_names = serializers.SerializerMethodField()

    class Meta:
        model = EntityAttribute
        fields = ('name', 'title', 'attr_names',)

    def get_attr_names(self, obj):
        attr_names = []
        if obj.attributes:
            for attr in obj.attributes.values('name'):
                attr_names.append(attr['name'])
        return attr_names



class EntityAttributeSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntityAttribute
        fields = ('name', 'title',)
