from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    createdby = models.CharField(max_length=255)
