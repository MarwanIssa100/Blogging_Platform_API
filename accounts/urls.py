from django.urls import path, include
from .views import UserRegistrationView, UserLoginView , UserProfileUpdateView , UserListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/<int:user_id>' , UserProfileUpdateView.as_view(), name='update'),
    path('users/' , UserListView.as_view(), name='users'),
]