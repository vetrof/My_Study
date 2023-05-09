from basket.models import Basket


def baskets(request):
    user = request.user
    username = user.username

    if username:
        return {'baskets': Basket.objects.filter(
            user=user) if user.is_authenticated else [],
                'baskets_product_id': Basket.objects.filter(
                    user=user).values_list('product', flat=True),
                }
    else:
        return {'baskets': Basket.objects.filter(
            user=user) if user.is_authenticated else []
                }



