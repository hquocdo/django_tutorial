from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('create/',views.PostCreate.as_view())
   
  ]
