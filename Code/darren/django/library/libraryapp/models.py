from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.IntegerField()
    pages = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_checked_out(self):
        return self.checkouts.filter(date_checkin__isnull=True).exists()

class BookCheckout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='checkouts')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='checkouts')
    date_checkout = models.DateTimeField(auto_now_add=True)
    date_checkin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book.title
