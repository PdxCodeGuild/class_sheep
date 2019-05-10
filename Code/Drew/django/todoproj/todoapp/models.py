from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
