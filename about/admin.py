from django.contrib import admin
from .models import AboutPage

class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    list_display_links = ['pk', 'title']

admin.site.register(AboutPage, AboutPageAdmin)