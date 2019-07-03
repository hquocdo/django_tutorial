from django.views.generic import DetailView
from .models import Post 
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework	import pagination
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse , HttpResponse
from django.core import serializers
class PostCreate(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class StandardResults(pagination.PageNumberPagination) :
	page_size = 6
	page_size_query_param = 'size'
	max_size = 100
class PostList(generics.ListAPIView) :
	serializer_class = PostSerializer
	pagination_class = StandardResults
	def get_queryset(self) :
		queryset_list = Post.objects.all()
		query = self.request.query_params.get('query',None)
		print(query)
		if query :
			queryset_list = queryset_list.filter(author__username=query).aggregate(Avg('mark'))
		return queryset_list
def GetAuthorDetail(request ,author) :
	author_posts = Post.objects.filter(author__username=author)
	data = serializers.serialize('json',author_posts)
	return HttpResponse(data)
class AuthorList(generics.ListAPIView) :
	serializer_class = PostSerializer
	lookup_url_kwarg = "author"
	def get_queryset(self) :
		author = self.kwargs.get(self.lookup_url_kwarg)
		authorlist = Post.objects.filter(author__username=author)
		return authorlist
def GetAuthorAvg(request ,author) :
	author_posts = Post.objects.filter(author__username=author).aggregate(Avg('mark'))
	return JsonResponse(author_posts)
class PostDetail(generics.RetrieveUpdateDestroyAPIView) :
	queryset = Post.objects.all()
	serializer_class = PostSerializer
