from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author
from django.utils import timezone


def index(request):
    books_list = Book.objects.all()
    context = {
        'books_list': books_list
    }
    return render(request, 'libraryapp/index.html', context)

def checkout(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.check_out_date = timezone.now()
    book.save()
    context = {
        'book': book,
    }
    return render(request, 'libraryapp/checkout.html', context)

def checkin(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.check_out_date = None
    book.save()
    context = {
        'book': book,
    }
    return render(request, 'libraryapp/checkin.html', context)


# def hide_button(request):
#     book = Book.objects.get(pk=book_id)
#     for book in book_list:
#         if book.check_out_date
#     return HttpResponseRedirect(reverse('libraryapp:index'))
