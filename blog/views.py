from rest_framework.views import  APIView
from .serializers import BlogSerializer , CategorySerializer , TagSerializer
from .models import Blog , Category , Tag
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from rest_framework.generics import GenericAPIView
# Create your views here.

class BlogCreationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class BlogDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=200)
    
class BlogUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer = BlogSerializer(blog, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
class BlogDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        blog.delete()
        return Response(status=204)
    
class TagCreationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TagDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        tag = Tag.objects.get(id=kwargs['id'])
        tag.delete()
        return Response(status=204)
    
class CategoryCreationView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q','')
        blogs = Blog.objects.filter(Q(Title__icontains=query) 
                                    | Q(Content__icontains=query)|Q(tags__name__icontains=query)|Q(Author__username__icontains=query))
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)
    
class BlogFilterationView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('Category','')
        author = request.query_params.get('Author','')
        blogs = Blog.objects.filter(Q(Category__name=category) |Q(Author__username=author))
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)
