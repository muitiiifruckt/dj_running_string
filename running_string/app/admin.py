# admin.py
from django.contrib import admin
from .models import VideoRequest

@admin.register(VideoRequest)
class VideoRequestAdmin(admin.ModelAdmin):
    list_display = ('text', 'output_file', 'created_at')
