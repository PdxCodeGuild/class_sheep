from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, reverse
from .models import Author, Genre, Book
from django.utils import timezone

def index(request):
    return render(request, 'libraryapp/index.html')

def author_index(request):
    context = {
        'message': 'List by Authors',
        'authors': Author.objects.all()
    }
    return render(request, 'libraryapp/author_index.html', context)

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    #book_list = get_object_or_404(Book, pk=author_id)
    context = {
        'author': author,
        'name': author.name,
        'books': author.books.all(),
    }
    return render(request, 'libraryapp/author_detail.html', context)

def book_index(request):
    context = {
        'message': 'List by Books',
        'books': Book.objects.all()
    }
    return render(request, 'libraryapp/book_index.html', context)

def book_detail(request, book_id):
    response = "stock text."
    return HttpResponse(response)

def checkout(request):
    return HttpResponse("You're looking at the checkout page.")
