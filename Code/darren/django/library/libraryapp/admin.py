from django.contrib import admin
from .models import Author, Genre, Book, BookCheckout

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookCheckout)
