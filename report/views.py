from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Post 
from .serializers import PostSerializer
from rest_framework import generics

# Create your views here.
class PostList(generics.ListAPIView) :
	queryset = Post.objects.all()
	serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView) :
	queryset = Post.objects.all()
	serializer_class = PostSerializer