from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    text= models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.text

    def published_date(self):
        return self.pub_date
