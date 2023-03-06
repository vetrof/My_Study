from django.db import models
from houses.models import House

# Create your models here.


class Order(models.Model):
    house = models.ForeignKey(House, verbose_name='Дом', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    email = models.EmailField('Email(не обязательно)', default='')
    date = models.DateTimeField('Дата', auto_now_add=True)
