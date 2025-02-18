from django.db import models
from django.conf import settings
from buddy_requests.models import Buddy

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class ChatMessage(models.Model):
    """
    Model to store chat messages between two users (buddies).
    """
    buddy = models.ForeignKey(Buddy, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message from {self.sender} to {self.buddy.recipient} at {self.timestamp}"

    panels = [
        FieldPanel("message")
    ]