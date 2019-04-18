from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_todo_items(self):
        return self.items.filter(date_completed_isnull=True)

    def get_completed_items(self):
        return self.items.filter(date_completed_isnull=False)

    def __str__(self):
        return self.text

class TodoItem(models.Model):
    text = models.TextField()
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()

    def completed(self):
        return self.date_completed is not None

    def __str__(self):
        return self.list.text + ': ' + self.text
