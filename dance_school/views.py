from django.http import HttpResponse
from django.shortcuts import render

__all__ = [
    "home",
    "test_view",
    "about",
    "register",
]

#def home(request):
 #   return HttpResponse("Hello, World!")

def test_view(request):
    return HttpResponse("View di prova con HttpResponse")

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")
