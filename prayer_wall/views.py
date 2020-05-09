from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Prayer Wall Home Page</h1>")

def about(request):
    return HttpResponse("<h1>Prayer Wall About Page</h1>")
