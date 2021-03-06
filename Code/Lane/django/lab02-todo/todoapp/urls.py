from django.urls import path

from . import views

app_name = 'todoapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('completed_todo/<int:id_num>/', views.completed_todo, name='completed')
]
