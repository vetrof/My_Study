# Generated by Django 4.1.6 on 2023-02-21 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_house_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['-active', 'name'], 'verbose_name': 'Дом', 'verbose_name_plural': 'Дома'},
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='houses.house')),
            ],
        ),
    ]
