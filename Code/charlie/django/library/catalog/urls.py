from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('index/', views.index, name='index')
]
