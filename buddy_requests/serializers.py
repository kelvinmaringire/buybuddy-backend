from rest_framework import serializers

from .models import BuddyRequest, Buddy, ReviewBuddy, Notification


class BuddyRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuddyRequest
        fields = '__all__'


class BuddySerializer(serializers.ModelSerializer):

    class Meta:
        model = Buddy
        fields = '__all__'


class ReviewBuddySerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewBuddy
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'
