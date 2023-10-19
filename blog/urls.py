from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", blog_view, name='index'),
    path('<int:pid>', blog_single, name="single"),
    path('category/<str:cat_name>', blog_category, name="blog_category"),

    # path('<int:pid>', test, name="test")
    path('test', test, name="test")

]
    
 