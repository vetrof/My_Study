from django.contrib import admin
from products.models import Product, ProductCategory, Basket


admin.site.register(ProductCategory)
# admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category', 'stripe_product_price_id', 'id')
    fields = ('name', 'description', 'category', ('price', 'quantity'), 'stripe_product_price_id','image')
    # readonly_fields = []
    search_fields = ('name', 'description')
    ordering = ('-id',)


# @admin.register(Basket)
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
