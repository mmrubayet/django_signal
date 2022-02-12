from django.urls import path
from .views import (
    HomePageView,
    BlogListView, BlogDetailView, BlogCreateView,
    PostListView, PostDetailView, PostCreateView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='new_blog'),

    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='new_post'),

]
