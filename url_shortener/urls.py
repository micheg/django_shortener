from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Reindirizza la root alla vista di login
    path('', include('shortener.urls')),
]
