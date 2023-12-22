from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from conversation.models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    conversation_serializer = ConversationSerializer(conversations, many=True)
    return Response(conversation_serializer.data)
