# Generated by Django 4.1.6 on 2023-02-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_alter_house_options_house_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]
