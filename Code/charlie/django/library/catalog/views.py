from django.shortcuts import render
from django.http import HttpResponse


from .models import Book, Author

def index(request):
    book_list = Book.objects.all()
    # print(book_list)
    context = {
        'booklist':book_list
    }
    return render(request, 'catalog/index.html', context)
