from django.urls import path
from .views import UserRegistrationView, UserLoginView , UserProfileUpdateView , UserListView , UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/<int:user_id>' , UserProfileUpdateView.as_view(), name='update'),
    path('users/' , UserListView.as_view(), name='users'),
    path('logout/' , UserLogoutView.as_view(), name='logout'),
    
]