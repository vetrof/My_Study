from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from basket.models import Basket
from lessons.models import Lessons


@login_required # метод переопределен в моделс
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    x = request.META['HTTP_REFERER']
    revers_link = request.META['HTTP_REFERER']
    # revers_link_to_basket = f"{settings.DOMAIN_NAME}/cabinet/{request.user.id}"
    return HttpResponseRedirect(revers_link)


@login_required()
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
