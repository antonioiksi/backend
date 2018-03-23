from rest_framework import serializers

from .models import Log


class LogSerializer(serializers.ModelSerializer):
    query = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = ('user', 'ip', 'datetime', 'query', 'event', 'method')

    def get_query(self, obj):
        attr_name = obj.query['query']['bool']['should'][0]['query_string']['default_field']
        attr_val = obj.query['query']['bool']['should'][0]['query_string']['query']
        return attr_name+':'+attr_val


class LogSimpleSerializer(serializers.Serializer):
    ip = serializers.CharField(required=True, allow_blank=False, max_length=100)
    event = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Log` instance, given the validated data.
        """
        return Log.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Log` instance, given the validated data.
        """
        instance.ip = validated_data.get('ip', instance.ip)
        instance.event = validated_data.get('event', instance.event)
        instance.save()
        return instance
