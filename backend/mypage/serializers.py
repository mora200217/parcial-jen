# mypage/serializers.py
from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False, allow_blank=True)
    price = serializers.FloatField()
    calories = serializers.IntegerField(required=False)
    available = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        from .models import Food
        return Food(**validated_data).save()

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
