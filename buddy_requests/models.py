from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from accounts.models import CustomUser
from stores.models import Deal


@register_snippet
class BuddyRequest(models.Model):
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_requests')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_requests')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='buddy_requests')
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')
                                                      ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username} to {self.recipient.username} for {self.deal.title}"

    panels = [
        FieldPanel("requester"),
        FieldPanel("recipient"),
        FieldPanel("deal"),
        FieldPanel("status"),
    ]


@register_snippet
class Buddy(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='buddies_as_user1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='buddies_as_user2')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    confirmed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1.username} & {self.user2.username} for {self.deal.title}"

    panels = [
        FieldPanel("user1"),
        FieldPanel("user2"),
        FieldPanel("deal"),
    ]


@register_snippet
class ReviewBuddy(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='given_reviews')
    buddy = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_reviews')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.buddy.username}"

    panels = [
        FieldPanel("reviewer"),
        FieldPanel("buddy"),
        FieldPanel("deal"),
        FieldPanel("rating"),
        FieldPanel("comment"),
    ]


@register_snippet
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"

    panels = [
        FieldPanel("user"),
        FieldPanel("message"),
        FieldPanel("read"),
    ]

