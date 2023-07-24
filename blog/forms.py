from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPage


class BlogPageForm(forms.ModelForm):
    class Meta:
        model = BlogPage
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(),
        }
