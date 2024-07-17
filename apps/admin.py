
from django.contrib import admin

from apps.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = 'slug',


@admin.register(Category)
class IconicAdmin(admin.ModelAdmin):
    exclude = 'slug',