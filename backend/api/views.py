from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemList(APIView):
    # GET: listar
    def get(self, request):
        items = Item.objects()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    # POST: crear
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    # GET: obtener uno
    def get(self, request, pk):
        item = Item.objects(id=pk).first()
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    # PUT: actualizar
    def put(self, request, pk):
        item = Item.objects(id=pk).first()
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: eliminar
    def delete(self, request, pk):
        item = Item.objects(id=pk).first()
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
