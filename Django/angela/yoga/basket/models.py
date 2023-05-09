from django.db import models

from lessons.models import Lessons, OrderingLessons, Pay_lessons
from users.models import User


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
    product = models.ForeignKey(to=Lessons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт {self.product.name} {self.user.id}'

    def summ(self):
        return self.product.price * self.quantity


    def de_json(self):

        user = self.user.username
        lesson_name = self.product.name
        id_lesson = self.product.id
        video_link = self.product.short_info

        OrderingLessons.objects.create(id_lesson=id_lesson,
                                       user=user,
                                       video_link=video_link,
                                       lesson_name=lesson_name,
                                       id_lesson_int=id_lesson)

        user_id = self.user.id
        lesson_id = self.product.id
        Pay_lessons.objects.create(user_id=user_id, lesson_id=lesson_id)


        basket_item = {
            'product_id': self.product.id,
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
            basket.quantity = 1
            basket.save()
            is_crated = False
            return basket, is_crated




