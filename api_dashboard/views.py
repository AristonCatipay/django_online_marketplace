from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from item.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_current_user_items(request):
    items = Item.objects.filter(created_by=request.user)
    item_serializer = ItemSerializer(items, many=True)
    return Response(item_serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_current_user_item(request, item_primary_key):
    item = get_object_or_404(Item, pk=item_primary_key)
    if item.created_by == request.user:
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('This is not your item.', status=status.HTTP_400_BAD_REQUEST)