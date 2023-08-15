from django.shortcuts import HttpResponse

# Create your views here.
def homeView(request):
    return HttpResponse('<h1>Home</h1>')