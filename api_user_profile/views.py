from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from user_profile.models import Profile
from .serializers import ProfileSerializer, UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_current_user_profile(request):
    current_user_profile = get_object_or_404(Profile, user=request.user)
    profile_serializer = ProfileSerializer(current_user_profile, many=False)
    return Response(profile_serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_current_user_profile(request):
    current_user_profile = get_object_or_404(Profile, user=request.user)
    profile_serializer = ProfileSerializer(current_user_profile, data=request.data)
    if profile_serializer.is_valid():
        profile_serializer.save()
        return Response(profile_serializer.data)
    return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_current_user(request):
    current_user = get_object_or_404(User, pk=request.user.id)
    user_serializer = UserSerializer(current_user, data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)