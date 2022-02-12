from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Post, Blog


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'author', 'body']


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title_ps', 'author_ps', 'body_ps']
