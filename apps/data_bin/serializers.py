from rest_framework import serializers

from .models import Bin, BinItem


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('user','name',)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if len(data['name']) < 2:
            raise serializers.ValidationError("'name' must contain more than 2 symbols")
        return data

class BinItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinItem
        fields = ('bin','query','data','mapping',)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if len(data['data']) < 2:
            raise serializers.ValidationError("'data' must contain more than 2 symbols")
        return data
