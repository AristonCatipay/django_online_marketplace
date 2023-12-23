from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from item.models import Item
from conversation.models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, ConversationMessageContentSerializer

def check_if_user_is_a_conversation_member(user, conversation):
    if user not in conversation.members.all():
        return Response({"detail": "You are not a member of this conversation."}, status=status.HTTP_403_FORBIDDEN)
    return None

def check_if_user_owns_the_item(user, item):
    if item.created_by == user:
        return Response({"detail": "You are the owner of this item."}, status=status.HTTP_403_FORBIDDEN)
    return None

def check_if_user_already_messaged_owner(user, item):
    conversations = Conversation.objects.filter(item=item).filter(members__in=[user.id]).exists()
    if conversations:
        return Response({"detail": "You already messaged the owner before."}, status=status.HTTP_403_FORBIDDEN)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_conversation(request, item_primary_key):
    item = get_object_or_404(Item, pk=item_primary_key)

    is_owner = check_if_user_owns_the_item(request.user, item)
    if is_owner:
        return is_owner

    messaged_before = check_if_user_already_messaged_owner(request.user, item)
    if messaged_before:
        return messaged_before

    conversation_message_content_serializer = ConversationMessageContentSerializer(data=request.data)
    if conversation_message_content_serializer.is_valid():
        conversation = Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(item.created_by)
        conversation.save()
        
        conversation_message_content_serializer.save(conversation=conversation, created_by=request.user)
        return Response(conversation_message_content_serializer.data)
    return Response(conversation_message_content_serializer.errors, status=status.HTTP_400_BAD_REQUEST)