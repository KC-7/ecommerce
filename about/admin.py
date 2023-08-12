from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import AboutPage


class AboutPageAdminForm(forms.ModelForm):
    """ Add CKEditor to admin for about page """
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutPage
        fields = '__all__'


class AboutPageAdmin(admin.ModelAdmin):
    """ Admin for about page """
    form = AboutPageAdminForm
    list_display = ['pk', 'title', 'created_at']
    list_display_links = ['pk', 'title']
    search_fields = ['title', 'content']
    list_filter = ['created_at']


admin.site.register(AboutPage, AboutPageAdmin)
