from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True)

    def __str__(self):
        return self.text
