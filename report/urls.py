from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('Post/', views.PostList.as_view()),
    path('Post/<int:pk>/',views.PostDetail.as_view()),
    path('Post/create/',views.PostCreate.as_view()),
    path('Post/<author>',views.AuthorList.as_view()),
    path('Post/mark/<author>',views.GetAuthorAvg)
    ]
