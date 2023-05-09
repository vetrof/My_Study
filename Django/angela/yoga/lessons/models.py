from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from taggit.managers import TaggableManager

import stripe

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderingLessons(models.Model):
    id_lesson = models.CharField('id урока', max_length=25)
    user = models.CharField('user', max_length=25)
    lesson_name = models.CharField('lesson name', max_length=128, null=True,
                                   blank=True)
    lesson_description = models.TextField('info', null=True,
                                          blank=True)
    image = models.ImageField('фото', upload_to='lessons/photos', default='',
                              blank=True)
    video_link = models.CharField('video_link', max_length=256, default='')

    id_lesson_int = models.IntegerField('id unt', null=True,
                                        blank=True)

    def __str__(self):
        return f'{self.id_lesson} {self.lesson_name} | {self.user}'


class LessonsCategory(models.Model):
    name = models.CharField('Название', max_length=128)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Lessons(models.Model):
    name = models.CharField('Название', max_length=128)
    short_info = models.CharField('Коротко', max_length=250,
                                  default='краткое описание')
    description = models.TextField('Описание')
    image = models.ImageField('фото', upload_to='lessons/photos', default='',
                              blank=True)
    free = models.BooleanField('Бесплатно?', default=False)
    price = models.IntegerField('Цена')
    active = models.BooleanField('Активен', default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=LessonsCategory, on_delete=models.CASCADE)
    tags = TaggableManager()
    stripe_product_price_id = models.CharField(max_length=128, null=True,
                                               blank=True)

    ordering_user = models.ForeignKey(to=OrderingLessons, null=True,
                                      on_delete=models.CASCADE, blank=True)

    video_link = models.CharField('Видео ссылка', max_length=250,
                                  default='--')

    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        blank=True
    )
    create_at = models.DateTimeField(auto_now_add=True, null=True,
                                     blank=True)

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return f'{self.id} {self.name} | {self.category} | {self.tags}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Lessons, self).save(force_insert=False, force_update=False,
                                  using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100),
            currency='rub')
        return stripe_product_price


class Pay_lessons(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(to=Lessons, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.lesson}'
