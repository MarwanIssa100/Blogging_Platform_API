from django.urls import path
from .views import BlogCreationView , BlogDetailsView , BlogUpdateView , BlogDeleteView , CategoryCreationView, SearchView, BlogFilterationView, TagDeleteView , BlogListView

urlpatterns = [
    path('create/', BlogCreationView.as_view(), name='create'),
    path('details/<int:id>/', BlogDetailsView.as_view(), name='details'),
    path('update/<int:id>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BlogDeleteView.as_view(), name='delete'),
    path('list/', BlogListView.as_view(), name='list'),
    path('tag/delete/<int:id>/', TagDeleteView.as_view(), name='tag_delete'),
    path('category/create/', CategoryCreationView.as_view(), name='category_create'),
    path('search/', SearchView.as_view(), name='search'),
    path('filter/', BlogFilterationView.as_view(), name='filter'),
]