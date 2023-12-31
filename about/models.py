from django.db import models
from ckeditor.fields import RichTextField


class AboutPage(models.Model):
    """ Model for about page """
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
