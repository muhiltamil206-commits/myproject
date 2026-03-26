
from django.shortcuts import render, redirect

from django.http import HttpResponse


def homeContent(request):
    return render(request, "secondApp/home.html")

def aboutContent(request):
    return render(request, "secondApp/about.html")

