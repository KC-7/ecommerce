from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import AboutPage


class AboutPageForm(forms.ModelForm):
    """ Form for about page """
    class Meta:
        model = AboutPage
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control rounded-2'}),
            'content': CKEditorWidget(
                attrs={'class': 'form-control rounded-2'}),
        }
