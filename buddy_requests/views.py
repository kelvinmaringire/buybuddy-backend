from rest_framework import generics

from .models import BuddyRequest, Buddy, ReviewBuddy, Notification
from .serializers import BuddyRequestSerializer, BuddySerializer, ReviewBuddySerializer, NotificationSerializer


class BuddyRequestListCreate(generics.ListCreateAPIView):
    queryset = BuddyRequest.objects.all()
    serializer_class = BuddyRequestSerializer


class BuddyRequestUpdate(generics.RetrieveUpdateAPIView):
    queryset = BuddyRequest.objects.all()
    serializer_class = BuddyRequestSerializer


class BuddyListCreate(generics.ListCreateAPIView):
    queryset = Buddy.objects.all()
    serializer_class = BuddySerializer


class BuddyUpdate(generics.RetrieveUpdateAPIView):
    queryset = Buddy.objects.all()
    serializer_class = BuddySerializer


class ReviewBuddyListCreate(generics.ListCreateAPIView):
    queryset = ReviewBuddy.objects.all()
    serializer_class = ReviewBuddySerializer


class ReviewBuddyUpdate(generics.RetrieveUpdateAPIView):
    queryset = ReviewBuddy.objects.all()
    serializer_class = ReviewBuddySerializer


class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationUpdate(generics.RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
