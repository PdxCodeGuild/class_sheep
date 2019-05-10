
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp_projurlpath/', include('todoapp.urls_in_app')),
]
