# Generated by Django 4.2.6 on 2023-11-06 09:48

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_culturepost_next_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='category',
            field=models.CharField(choices=[('FOOD', 'Питание'), ('LEISURE', 'Досуг'), ('OTHER', 'Другое')], default=posts.models.Categories['OTHER'], max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='subcategory',
            field=models.CharField(choices=[('MUSEUMS', 'Музеи'), ('CINEMAS', 'Кинотеатры'), ('CAFFE', 'Кафе'), ('SHOPPING_CENTERS', 'Торгово-развлекательные центры'), ('RESTAURANTS', 'Рестораны'), ('ACTIVE_LEISURE', 'Активный отдых'), ('BARS', 'Бары'), ('CONCERT_HALLS', 'Концертные и выставочные залы'), ('THEATERS', 'Театры'), ('OTHER', 'Другое')], default=(('MUSEUMS', 'Музеи'), ('CINEMAS', 'Кинотеатры'), ('CAFFE', 'Кафе'), ('SHOPPING_CENTERS', 'Торгово-развлекательные центры'), ('RESTAURANTS', 'Рестораны'), ('ACTIVE_LEISURE', 'Активный отдых'), ('BARS', 'Бары'), ('CONCERT_HALLS', 'Концертные и выставочные залы'), ('THEATERS', 'Театры'), ('OTHER', 'Другое')), max_length=100, verbose_name='Вторичная категория'),
        ),
    ]