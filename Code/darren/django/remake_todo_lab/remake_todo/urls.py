from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:list_id>/detail/', views.detail, name='detail'),
    path('<int:list_id>/save_todo/', views.save_todo, name='save_todo')
]
