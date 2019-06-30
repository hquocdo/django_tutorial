from django.views.generic import DetailView
from .models import Post 
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework	import pagination
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated

class PostCreate(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class StandardResults(pagination.PageNumberPagination) :
	page_size = 5
class PostList(generics.ListAPIView) :
	serializer_class = PostSerializer
	pagination_class = StandardResults
	def get_queryset(self) :
		request = self.request
		print(request.user)
		queryset_list = Post.objects.all()
		query = self.request.GET.get("q")
		print(query)
		if query :
			queryset_list = queryset_list.filter(author__username=query)		
		return queryset_list
class PostDetail(generics.RetrieveUpdateDestroyAPIView) :
	queryset = Post.objects.all()
	serializer_class = PostSerializer
