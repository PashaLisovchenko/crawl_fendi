from django.contrib import admin
from .models import Product, Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'url', 'categories']


admin.site.register(Product, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['url', 'product']


admin.site.register(Image, ImageAdmin)
