import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from django.forms.models import model_to_dict

from buddy_requests.models import Buddy
from accounts.models import CustomUser
from .models import ChatMessage

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        room_name = text_data_json["roomName"]
        sender = text_data_json["sender"]

        buddy = Buddy.objects.get(id=int(room_name))
        user = CustomUser.objects.get(id=int(sender))

        chat_message = ChatMessage.objects.create(
            buddy=buddy,
            message=message,
            sender=user
        )

        chat_message_dict = model_to_dict(chat_message)
        chat_message_dict['timestamp'] = chat_message.timestamp.isoformat()
        chat_message_dict['type'] = "chat_message"
        print(chat_message_dict)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, chat_message_dict)

    # Receive message from room group
    def chat_message(self, event):
        buddy = event["buddy"]
        sender = event["sender"]
        message = event["message"]
        timestamp = event["timestamp"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "buddy": buddy,
            "sender": sender,
            "message": message,
            "timestamp": timestamp
        }))
