from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class BlogListView(ListView):
    model = models.Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'
