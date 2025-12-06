from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        item = Item(**validated_data)
        item.save()
        return item

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
