from django.urls import path

from .views import ChatMessageListCreate


urlpatterns = [
    path('', ChatMessageListCreate.as_view()),
]