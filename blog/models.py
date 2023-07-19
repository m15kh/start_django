from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    content = models.TextField()