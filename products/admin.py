from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Lets the Admin know which Product fields will be displayed, 
    searched, and in what order (by sku).
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Lets the Admin know which Category fields will be displayed.
    """
    list_display = (
        'friendly_name',
        'name',
    )


# Registering the Product and Category classes in the admin.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
