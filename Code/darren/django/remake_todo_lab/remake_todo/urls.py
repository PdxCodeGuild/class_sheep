from django.urls import path

from . import views

app_name = 'remake_todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:list_id>/detail/', views.detail, name='detail'),
    path('save_todo_list/', views.save_todo_list, name='save_todo_list'),
    path('<int:list_id>/detail/add_todo/', views.add_todo, name='add_todo'),
    path('<int:list_id>/detail/mark_completed', views.mark_completed, name='mark_completed'),
    path('<int:list_id>/detail/mark_incomplete', views.mark_incomplete, name='mark_incomplete')
]
