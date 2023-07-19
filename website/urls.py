from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path("", index_view, name='index'),
    path("contact", contact_view, name='contact'), 
    path("about", about_view, name='about'),
    path("test", test_view, name='test')
]
    
