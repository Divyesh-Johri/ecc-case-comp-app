from django.db import models

# Create your models here.

class Announcements(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()