from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    """ Model for avatar """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/')
    punk_type = models.CharField(max_length=20)
    attributes = models.JSONField(default=dict)

    def __str__(self):
        return self.user.username

