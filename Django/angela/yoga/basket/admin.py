from django.contrib import admin

# Register your models here.
from basket.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)