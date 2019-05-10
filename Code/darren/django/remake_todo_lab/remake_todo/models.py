from django.db import models
from django.utils import timezone
import datetime

class List(models.Model):
    list_text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    # def get_todo_items(self):
    #     return self.items.filter(date_completed_isnull=True)

    # def get_completed_items(self):
    #     return self.items.filter(date_completed_isnull=False)
    #
    def was_published_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.list_text

class Todo(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='todos')
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()
    todo_text = models.CharField(max_length=200)

    # def completed(self):
    #     return self.date_completed is not None
    #
    def __str__(self):
        return self.list.list_text + ': ' + self.todo_text
