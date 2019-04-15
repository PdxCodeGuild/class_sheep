
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp_projurl/', include('todoapp.urls_app')),
]
