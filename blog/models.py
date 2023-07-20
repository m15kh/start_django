from django.db import models

# Create your models here.
class Post(models.Model):
    # author = 
    # img = 
    title = models.CharField(max_length=256)
    content = models.TextField()
    # category
    # tag
    counted_view = models.IntegerField()#default=0
    status = models.BooleanField()
        # create_date

    # published_date
    # uploaded_date

