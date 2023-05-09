from django.contrib import admin
from products.models import Product, ProductCategory, Basket


admin.site.register(ProductCategory)
# admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'price', 'category', )
    fields = ('name', 'description', 'category', ('price', 'quantity'), 'image')
    # readonly_fields = []
    search_fields = ('name', 'description')
    ordering = ('-id',)


# @admin.register(Basket)
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
