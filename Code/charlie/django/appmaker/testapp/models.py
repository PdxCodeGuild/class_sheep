from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    checked_out = models.BooleanField()

    def __str__(self):
        return f'{self.text} {self.pub_date}'
