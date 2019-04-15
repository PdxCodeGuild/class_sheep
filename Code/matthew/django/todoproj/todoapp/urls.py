
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('view2/', views.view2),
]
