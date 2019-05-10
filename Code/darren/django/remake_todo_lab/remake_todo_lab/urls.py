from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('remake_todo/', include('remake_todo.urls')),
]
