from django.contrib import admin

from .models import ShoplistProduct, Category, Gallery, Color, Size


admin.site.register(Category)


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class ColorInline(admin.TabularInline):
    fk_name = 'add_color'
    model = Color


class SizeInline(admin.TabularInline):
    fk_name = 'add_size'
    model = Size


@admin.register(ShoplistProduct)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ColorInline, SizeInline]

