from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'has_sizes',
        'image_preview',
    )

    search_fields = ['sku', 'name']
    list_filter = ('category', 'has_sizes')
    ordering = ('sku',)

    actions = ['products_have_sizes', 'products_dont_have_sizes']

    def products_have_sizes(self, request, queryset):
        queryset.update(has_sizes=True)
        self.message_user(
            request, "Sizes have been added to the selected products."
            )

    def products_dont_have_sizes(self, request, queryset):
        queryset.update(has_sizes=False)
        self.message_user(
            request, "Sizes have been removed from the selected products."
            )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
