from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class SighUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name ='registration/sighup.html'