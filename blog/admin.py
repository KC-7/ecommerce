from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPage

class BlogPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPage
        fields = '__all__'

class BlogPageAdmin(admin.ModelAdmin):
    form = BlogPageAdminForm
    list_display = ['pk', 'title', 'created_at']
    list_display_links = ['pk', 'title']

admin.site.register(BlogPage, BlogPageAdmin)