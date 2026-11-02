from django.http import HttpResponse
from django.shortcuts import render

__all__ = [
    "home",
    "test_view",
    "about",
    "register",
    #"school_list",
    #"school_details",
]

#def home(request):
 #   return HttpResponse("Hello, World!")

def test_view(request):
    return HttpResponse("View di prova con HttpResponse")

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")

def school(request):
    return render(request, "school.html")

"""
def school_list(request):
    return render(request, "school_list.html")

def school_details(request):
    return render(request, "school_details.html")
"""