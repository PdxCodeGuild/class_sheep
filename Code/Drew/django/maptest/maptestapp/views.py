from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'maptestapp/index.html')

def glmap(request):
    return render(request, 'maptestapp/glmap.html')
