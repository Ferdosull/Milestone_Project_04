from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
