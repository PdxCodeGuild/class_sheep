from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/<int:todo_list_id>/', views.index, name='index'),
    path('todo_lists/', views.todo_lists, name='todo_lists'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('complete_todo/<int:todo_id>/', views.complete_todo, name='complete_todo')
]
