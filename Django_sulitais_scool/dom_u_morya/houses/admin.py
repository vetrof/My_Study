from django.contrib import admin
from houses.models import House
from houses.models import Gallery


# Register your models here.


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active']
    list_filter = ["active", 'price']
    inlines = [GalleryInline, ]



