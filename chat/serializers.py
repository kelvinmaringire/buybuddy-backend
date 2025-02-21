from rest_framework import serializers

from .models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = '__all__'

    def get_name(self, obj):
        return obj.sender.username
