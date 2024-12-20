from django.urls import path
from .views import BlogCreationView , BlogDetailsView , BlogUpdateView , BlogDeleteView

urlpatterns = [
    path('create/', BlogCreationView.as_view(), name='create'),
    path('details/<int:id>/', BlogDetailsView.as_view(), name='details'),
    path('update/<int:id>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BlogDeleteView.as_view(), name='delete'),  
]