from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from item.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_current_user_items(request):
    items = Item.objects.filter(created_by=request.user)
    item_serializer = ItemSerializer(items, many=True)
    return Response(item_serializer.data)
