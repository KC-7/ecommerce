from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import AboutPage

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(),
        }
