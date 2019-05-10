
from django.urls import path

from . import views

app_name = 'todoapp_urls_nickname'
urlpatterns = [
    path('index_appurlpath/', views.index_views_fun, name='index_path_nickname'),
    path('view2_appurlpath/', views.view2_views_fun, name='view2_path_nickname'),
    path('save_todo_appurlpath/', views.save_todo_views_fun, name='save_todo_path_nickname'),
]
