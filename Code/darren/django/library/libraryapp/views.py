from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, reverse
from .models import Author, Genre, Book
from django.utils import timezone

def index(request):
    return render(request, 'libraryapp/index.html')

def author_index(request):
    author_list = []
    for author in author_index:
        author_list.append(author)
    context = {
        'author_list': author_list,
    }
    return render(request, 'index/author_index.html', context)

def author_detail(request, author_id):
    response = "You're looking at author page %s."
    return HttpResponse(response % author_id)

def book_index(request):
    response = "You're looking at the books page"
    return HttpResponse(response)

def book_detail(request, book_id):
    response = "You're looking at book page %s."
    return HttpResponse(response % book_id)

def checkout(request):
    return HttpResponse("You're looking at the checkout page.")
