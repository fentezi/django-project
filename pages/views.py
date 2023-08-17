from django.views.generic import ListView, TemplateView
from . import models

class HomePageView(ListView):
    model = models.Post
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'