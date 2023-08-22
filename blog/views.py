from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = models.Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
    model = models.Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'author', 'body', ]


class BlogUpdateView(UpdateView):
    model = models.Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body', ]


class BlogDeleteView(DeleteView):
    model = models.Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy("blog:home")
