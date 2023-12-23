from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from conversation.models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, ConversationMessageContentSerializer

def check_if_user_is_a_conversation_member(user, conversation):
    if user not in conversation.members.all():
        return Response({"detail": "You are not a member of this conversation."}, status=status.HTTP_403_FORBIDDEN)
    return None

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    conversation_serializer = ConversationSerializer(conversations, many=True)
    return Response(conversation_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_conversation_messages(request, conversation_primary_key):
    conversation = get_object_or_404(Conversation, pk=conversation_primary_key)

    is_conversation_member = check_if_user_is_a_conversation_member(request.user, conversation)
    if is_conversation_member:
        return is_conversation_member
        
    conversations = Conversation.objects.filter(members__in=[request.user.id]).get(id=conversation_primary_key)
    conversation_messages_serializer = ConversationMessageSerializer(conversations.messages, many=True)
    return Response(conversation_messages_serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request, conversation_primary_key):
    conversation = get_object_or_404(Conversation, pk=conversation_primary_key)

    is_conversation_member = check_if_user_is_a_conversation_member(request.user, conversation)
    if is_conversation_member:
        return is_conversation_member

    conversation_message_content_serializer = ConversationMessageContentSerializer(data=request.data)
    if conversation_message_content_serializer.is_valid():
        conversation_message_content_serializer.save(conversation=conversation, created_by=request.user)
        return Response(conversation_message_content_serializer.data)
    return Response(conversation_message_content_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
