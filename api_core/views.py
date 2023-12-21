from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout as django_logout
from .serializers import ItemSerializer, CategorySerializer, SignUpSerializer, UserSerializer
from item.models import Item, Category
from user_profile.models import Profile

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

@api_view(['POST'])
def signup(request):
    signup_serializer = SignUpSerializer(data=request.data)
    
    if signup_serializer.is_valid():
        validated_data = signup_serializer.validated_data
        email = validated_data['email']
        username = validated_data['username']
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(**validated_data)
            
            profile = Profile.objects.create(user=user)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # User is authenticated.
        auth.login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        # Invalid credentials
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    django_logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)