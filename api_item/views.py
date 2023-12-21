from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import ItemSerializer
from item.models import Item, Category


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_item_detail(request, item_primary_key):
    item = get_object_or_404(Item, id=item_primary_key)
    seller_profile = item.created_by.profile
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=item_primary_key)[0:3]
    serializer = ItemSerializer(item)
    serialized_item = serializer.data

    serialized_item['seller'] = {
        'first_name': seller_profile.user.first_name,
        'last_name': seller_profile.user.last_name,
        'username': seller_profile.user.username,
        'email': seller_profile.user.email,
        'location': seller_profile.location,
    }
    serialized_related_items = ItemSerializer(related_items, many=True).data

    response_data = {
        'item': serialized_item,
        'related_items': serialized_related_items,
    }

    return Response(response_data)

    