from http import HTTPStatus

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView, ListView, DetailView

import stripe
from basket.models import Basket
from order.forms import OrderForm
from order.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrdersListView(ListView):
    template_name = 'order/orders_list.html'
    title = 'Store - Заказы'
    queryset = Order.objects.all()
    ordering = ('-created')

    def get_queryset(self):
        queryset = super(OrdersListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderDetailView(DetailView):
    template_name = 'order/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - Заказ #{self.object.id}'
        print(context)
        return context


class OrderSuccessView(TemplateView):
    template_name = 'order/success.html'


class OrderCanceledView(TemplateView):
    template_name = 'order/cancled.html'


class OrderCreateView(CreateView):
    template_name = 'order/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=baskets.stripe_products(),
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body

    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_KEY
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Order.objects.get(id=order_id)
    order.update_after_payment()

