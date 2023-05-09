from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class OrderSerializer2(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['amount', 'description', 'user', 'products']
