from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'created',
        'email',
        'basket_history', 'status', 'initiator',
    )
    readonly_fields = ('id', 'created')
