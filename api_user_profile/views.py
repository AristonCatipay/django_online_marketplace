from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from user_profile.models import Profile
from .serializers import ProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_current_user_profile(request):
    current_user_profile = get_object_or_404(Profile, user=request.user)
    profile_serializer = ProfileSerializer(current_user_profile, many=False)
    return Response(profile_serializer.data)
