from django.contrib import admin
from django.utils.html import format_html
from .models import Avatar
from .generate import generate_and_save_punk_for_user  # assuming this is where your avatar generation function is

class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'show_avatar', 'punk_type', 'show_attributes')
    actions = ['generate_avatars_for_selected_users']

    def show_avatar(self, obj):
        try:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        except ValueError:
            return ''

    show_avatar.allow_tags = True
    show_avatar.short_description = 'Avatar'

    def show_attributes(self, obj):
        return ', '.join([f"{key}: {value}" for key, value in obj.attributes.items()])

    show_attributes.short_description = 'Attributes'

    def generate_avatars_for_selected_users(self, request, queryset):
        for avatar in queryset:
            generate_and_save_punk_for_user(avatar.user, request)
        self.message_user(request, f"Avatars generated for {queryset.count()} users.")


    generate_avatars_for_selected_users.short_description = "Generate avatars for selected users"

admin.site.register(Avatar, AvatarAdmin)

# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Avatar

# class AvatarAdmin(admin.ModelAdmin):
#     list_display = ('user', 'show_avatar', 'punk_type', 'show_attributes')

#     def show_avatar(self, obj):
#         try:
#             return format_html('<img src="{}" height="50" />', obj.image.url)
#         except ValueError:
#             return ''

#     show_avatar.allow_tags = True
#     show_avatar.short_description = 'Avatar'

#     def show_attributes(self, obj):
#         return ', '.join([f"{key}: {value}" for key, value in obj.attributes.items()])

#     show_attributes.short_description = 'Attributes'

# admin.site.register(Avatar, AvatarAdmin)
