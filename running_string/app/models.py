# models.py
from django.db import models

class VideoRequest(models.Model):
    text = models.TextField()
    output_file = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.text} at {self.created_at}"
