from django.contrib import admin
from .models import Contact


class ContactAdmon(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')


admin.site.register(Contact, ContactAdmon)
