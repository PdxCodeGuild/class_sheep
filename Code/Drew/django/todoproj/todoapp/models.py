from django.db import models
from django.utils import timezone

class ToDoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.todo_text
