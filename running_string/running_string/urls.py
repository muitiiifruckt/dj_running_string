from django.contrib import admin
from django.urls import path
from app import views  # Импорт представлений из вашего приложения

urlpatterns = [
    path('', views.create_video, name='create_video'),  # Маршрут для корневого URL
]