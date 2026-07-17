from django.urls import path
from users.views import UserRegistrationView, CurrentUserAPIView

urlpatterns = [
    path('users/register/', UserRegistrationView.as_view(), name='register'),
    path('users/me/', CurrentUserAPIView.as_view(), name='current-user'),
    ]