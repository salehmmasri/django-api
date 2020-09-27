from django.urls import path

from .views import PostsList, PostDetails

urlpatterns = [
    path('', PostsList.as_view(), name='posts'), # localhost:8000/api/v1/posts
    path('<int:pk>/', PostDetails.as_view(), name='post_details') # localhost:8000/api/v1/posts/1
]