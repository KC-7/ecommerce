from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPage
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from datetime import datetime


class BlogPageAdminForm(forms.ModelForm):
    """ Add CKEditor to admin for blog page """
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPage
        fields = '__all__'


class BlogPageAdmin(admin.ModelAdmin):
    """ Admin for blog page """
    form = BlogPageAdminForm
    list_display = [
        'pk', 'title', 'created_at_days_ago', 'short_content', 'preview_image']
    list_display_links = ['pk', 'title']
    readonly_fields = ['preview_image']
    search_fields = ['title', 'content']
    list_filter = ['created_at']

    def created_at_days_ago(self, obj):
        days_ago = (datetime.now().date() - obj.created_at.date()).days
        return f"{days_ago} days ago"
    created_at_days_ago.short_description = 'Created At'

    def short_content(self, obj):
        return format_html(truncatechars(obj.content, 100))
    short_content.short_description = 'Content'

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;">',
                obj.image.url)
        return "No Image"
    preview_image.short_description = 'Preview Image'

    ordering = ('-created_at', )


admin.site.register(BlogPage, BlogPageAdmin)
