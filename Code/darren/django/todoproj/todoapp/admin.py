from django.contrib import admin
from .models import TodoItem, TodoList

admin.site.register(TodoItem)
admin.site.register(TodoList)
