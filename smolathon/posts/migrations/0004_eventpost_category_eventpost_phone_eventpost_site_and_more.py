# Generated by Django 4.2.6 on 2023-10-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_delete_checkinurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpost',
            name='category',
            field=models.CharField(default='', max_length=100, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='phone',
            field=models.CharField(default='', max_length=50, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='Вебсайт'),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='subcategory',
            field=models.CharField(default='', max_length=100, verbose_name='Вторичная категория'),
        ),
        migrations.AlterField(
            model_name='culturepost',
            name='description',
            field=models.TextField(default='', max_length=400, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='description',
            field=models.TextField(default='', max_length=400, verbose_name='Описание'),
        ),
    ]
