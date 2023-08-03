from django import forms
from .widgets import CustomClearableFileInput
from ckeditor.widgets import CKEditorWidget
from .models import BlogPage


class BlogPageForm(forms.ModelForm):
    """ Form for blog page """
    class Meta:
        model = BlogPage
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control rounded-2'}),
            'content': CKEditorWidget(
                attrs={'class': 'form-control rounded-2'}),
        }

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
        )
