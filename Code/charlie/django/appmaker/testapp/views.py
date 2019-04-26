from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book, Author

def index(request):
    return HttpResponse("This is an HttpResponse, created in views.py")
