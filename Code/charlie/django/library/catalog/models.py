from django.db import models

import datetime

# Create your models here.
class Author(models.Model):
    """author information for a book"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Necessary attibutes for a book in a catalog ."""
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publish_date = models.DateField(null=True, blank=True)
    checked_out = models.BooleanField(null=True)

    def __str__(self):
        return self.title
