from django.db import models


# Create your models here.
class House(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    description = models.TextField('Описание')
    photo = models.ImageField('фотография', upload_to='houses/photos', default='', blank=True)
    active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['-active', 'name']

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
