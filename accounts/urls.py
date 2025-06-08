from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    UserListCreate,
    UserUpdate,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    ChangePasswordView
)


urlpatterns = [
    path('', UserListCreate.as_view()),
    path('<int:pk>/', UserUpdate.as_view()),
    path('password-reset/', PasswordResetRequestView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    ]
