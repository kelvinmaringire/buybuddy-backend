from rest_framework import generics

from .models import ChatMessage
from .serializers import ChatMessageSerializer


class ChatMessageListCreate(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer