from django.contrib import admin
from django.utils.html import format_html
from .models import Avatar


class AvatarAdmin(admin.ModelAdmin):
    """ Admin settings for Avatars """
    list_display = ('user', 'show_avatar', 'punk_type', 'show_attributes')

    def show_avatar(self, obj):
        try:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        except ValueError:
            return ''

    show_avatar.allow_tags = True
    show_avatar.short_description = 'Avatar'

    def show_attributes(self, obj):
        return ', '.join(
            [f"{key}: {value}" for key, value in obj.attributes.items()])

    show_attributes.short_description = 'Attributes'


admin.site.register(Avatar, AvatarAdmin)
