from django.db import models


from users.models import User


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
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id} | {self.name} | {self.category.name} | {self.price}'


# class BasketQuerySet(models.QuerySet):
#     def total_sum(self):
#         return sum(basket.summ() for basket in self)
#
#     def total_quantity(self):
#         return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    # objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина {self.user.email} | Продукт {self.product.name} / Остаток: {self.product.quantity}'

    def summ(self):
        return self.product.price * self.quantity



