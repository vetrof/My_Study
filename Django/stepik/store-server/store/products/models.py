import stripe
from django.db import models
from django.conf import settings

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images', null=True,
                              blank=True)
    stripe_product_price_id = models.CharField(max_length=128, null=True,
                                               blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id} | {self.name} | {self.category.name} | {self.price}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Product, self).save(force_insert=False, force_update=False,
                                  using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100),
            currency='rub')
        return stripe_product_price


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.summ() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина {self.user.email} | Продукт {self.product.name} / Остаток: {self.product.quantity}'

    def summ(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.summ()),
        }
        return basket_item

    @classmethod  # метод переопределен для совместимости с api
    def create_or_update(cls, product_id, user):
        baskets = Basket.objects.filter(user=user, product_id=product_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, product_id=product_id,
                                        quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated
