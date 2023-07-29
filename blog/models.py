from django.db import models

# Create your models here.
class Post(models.Model):
    # author = 
    # img = 
    title = models.CharField(max_length=256)
    content = models.TextField()
    # category
    # tag
    counted_view = models.IntegerField(default=0)#default=0
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   #2023-07-21 13:57:04.296657
    def __str__(self) -> str:
        return self.title