from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import AboutPage

class AboutPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutPage
        fields = '__all__'

class AboutPageAdmin(admin.ModelAdmin):
    form = AboutPageAdminForm
    list_display = ['pk', 'title', 'created_at']
    list_display_links = ['pk', 'title']

admin.site.register(AboutPage, AboutPageAdmin)