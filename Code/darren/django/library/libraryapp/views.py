from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, reverse
from .models import Author, Genre, Book, BookCheckout
from django.utils import timezone
import datetime

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
    book = Book.objects.get(pk=book_id)
    checked_out = book.is_checked_out()
    # author = book.author
    context = {
            'book': book,
            'author': book.author,
            'publish_date': book.publish_date,
            'pages': book.pages,
            'checked_out': checked_out,
            # 'author_id': Author.id.get(author)
    }
    return render(request, 'libraryapp/book_detail.html', context)

def checkout(request):
    context = {
        'message': 'Checkout Books',
        'books': Book.objects.all(),
        'book_checkout': BookCheckout.objects.all(),
    }
    return render(request, 'libraryapp/checkout.html', context)

def book_checkout(request, book_id):
    target_book = Book.objects.get(pk=book_id)
    bookcheck = target_book.is_checked_out()
    if bookcheck == True:
        print(bookcheck)
        checked_book = BookCheckout.objects.get(book_id=book_id)
        checked_book.date_checkin = datetime.datetime.now()
        print(BookCheckout.objects.all())
        book_returned_on = f'{checked_book.date_checkin.month}/{checked_book.date_checkin.day}'
        print(book_returned_on)
        checked_book.delete()
        return HttpResponseRedirect(reverse('libraryapp:checkout'))
    print(BookCheckout.objects.all())
    checked_book = BookCheckout(book_id=book_id, user=request.user)
    checked_book.save()
    book_checked_out_on = f'{checked_book.date_checkout.month}/{checked_book.date_checkout.day}'
    print(book_checked_out_on)
    return HttpResponseRedirect(reverse('libraryapp:checkout'))

def book_checkin(request, book_id):
    target_book.delete()
