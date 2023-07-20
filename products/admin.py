from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'has_sizes',
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
