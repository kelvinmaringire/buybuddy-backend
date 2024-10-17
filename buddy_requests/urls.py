from django.urls import path

from .views import (
    BuddyRequestListCreate,
    BuddyRequestUpdate,
    BuddyListCreate,
    BuddyUpdate,
    ReviewBuddyListCreate,
    ReviewBuddyUpdate,
    NotificationListCreate,
    NotificationUpdate,

)


urlpatterns = [
    path('', BuddyRequestListCreate.as_view()),
    path('<int:pk>/', BuddyRequestUpdate.as_view()),
    path('buddy/', BuddyListCreate.as_view()),
    path('buddy/<int:pk>/', BuddyUpdate.as_view()),
    path('review/', ReviewBuddyListCreate.as_view()),
    path('review/<int:pk>/', ReviewBuddyUpdate.as_view()),
    path('notification/', NotificationListCreate.as_view()),
    path('notification/<int:pk>/', NotificationUpdate.as_view()),
    ]
