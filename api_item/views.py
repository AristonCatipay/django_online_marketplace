from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import ItemSerializer
from item.models import Item, Category
from PIL import Image
import tempfile


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

def resize_and_compress_image(image, new_width, compression_quality=85, target_size_kb=100):
    # Calculate new height maintaining aspect ratio
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    
    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # Compress with iterative quality reduction to target a specific file size
    current_quality = compression_quality
    while True:
        temp_file.seek(0)
        resized_image.save(temp_file, format='JPEG', quality=current_quality)
        temp_file.seek(0)
        if temp_file.tell() / 1024 <= target_size_kb or current_quality <= 0:
            break
        current_quality -= 5  # Adjust the decrement value for quality
        
    temp_file.seek(0)
    return temp_file

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        try:
            # Retrieve image data from the request
            image_data = request.FILES.get('image')
            if image_data:
                # Open the image using PIL
                image = Image.open(image_data)
                
                # Resize and compress the image
                compressed_image = resize_and_compress_image(image, 600)
                
                # Save the compressed image to the item instance and the rest of the form
                serializer.validated_data['image'] = compressed_image.name

            # Set the created_by field to the current user
            serializer.validated_data['created_by'] = request.user

            # Save the item instance
            serializer.save()

            return Response(serializer.data)
        except Exception as e:
            return Response({'error': f"Error processing image: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, item_primary_key):
    item = get_object_or_404(Item, pk=item_primary_key)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)