from django.urls import path

from . import views

app_name = 'url_shortener'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('save/', views.save, name="save"),
    path('test/', views.test),
]