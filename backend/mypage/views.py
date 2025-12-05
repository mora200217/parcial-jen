# mypage/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

class FoodListCreateView(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
