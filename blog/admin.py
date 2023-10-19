from django.contrib import admin

# Register your models here.
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = 'empty'
    list_display = ['title','author', 'published_date', 'counted_view']
    list_filter  = ['author', 'status']
    search_fields = ['title', 'content']

admin.site.register( Category)
admin.site.register(Post, PostAdmin )
