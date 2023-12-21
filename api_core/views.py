from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer, CategorySerializer
from item.models import Item, Category

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_items_and_categories(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    item_categories = Category.objects.all()

    item_serializer = ItemSerializer(items, many=True)
    serialized_items = item_serializer.data

    category_serializer = CategorySerializer(item_categories, many=True)
    serialized_item_categories = category_serializer.data

    response_data = {
        'items' : serialized_items,
        'categories': serialized_item_categories,
    }

    return Response(response_data)