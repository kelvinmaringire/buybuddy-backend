from django.urls import path

from .views import (
    UserListCreate,
    UserUpdate,


)


urlpatterns = [
    path('', UserListCreate.as_view()),
    path('<int:pk>/', UserUpdate.as_view()),
    #path('change_password/', ChangePassword.as_view()),
    #path('password_reset/', PasswordReset.as_view()),
    #path('password_reset_confirm/', PasswordResetConfirm.as_view()),
    #path('token/', CustomTokenObtainPairView.as_view()),

    ]
