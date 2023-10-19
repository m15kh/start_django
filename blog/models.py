from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
 


class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.name




class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg' )
    title = models.CharField(max_length=256)
    content = models.TextField()
    post_category = models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_view = models.IntegerField(default=0)#default=0
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   #2023-07-21 13:57:04.296657

    class Meta:
        ordering = ['-published_date']



    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})


