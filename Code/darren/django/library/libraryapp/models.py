from django.db import models
from django.utils import timezone
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
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='authors')
    checked_out = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
