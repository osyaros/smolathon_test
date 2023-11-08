# Generated by Django 4.2.6 on 2023-11-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_eventpost_category_alter_eventpost_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturepost',
            name='description',
            field=models.TextField(blank=True, default='', max_length=400, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='category',
            field=models.CharField(default='', max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='description',
            field=models.TextField(blank=True, default='', max_length=400, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='subcategory',
            field=models.CharField(default='', max_length=100, verbose_name='Вторичная категория'),
        ),
    ]
