from django.db import models

class TodoItem_models_py(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
