from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


# html rendering
from orders.serializers2 import OrderSerializer2


def orders_page(request):

    for i in SalesOrder.objects.all():
        print(i.amount)

    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


# WEB Api with Django Rest http://127.0.0.1:8000/api/orders/?format=json
class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


# WEB Api test
class ApiSample(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer2
    # print(queryset)
