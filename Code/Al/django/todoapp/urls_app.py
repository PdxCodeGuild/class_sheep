
from django.urls import path

from . import views

app_name = 'todoapp_urls_py'
urlpatterns = [
    path('index_appurl/', views.index_views_fun, name='index_path'),
    path('view2_appurl/', views.view2_views_fun, name='view2_path'),
    path('save_todo_appurl/', views.save_todo_views_fun, name='save_todo_path'),
]
