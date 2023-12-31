# Generated by Django 4.2.6 on 2023-10-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_eventpost_category_eventpost_phone_eventpost_site_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='culturepost',
            options={'verbose_name': 'Исторический пост', 'verbose_name_plural': 'Исторические посты'},
        ),
        migrations.AlterModelOptions(
            name='eventpost',
            options={'verbose_name': 'Пост события', 'verbose_name_plural': 'Посты событий'},
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='is_unlimited_event_time',
            field=models.BooleanField(default=True, verbose_name='Время проведения неограничено'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='is_unlimited_working_time',
            field=models.BooleanField(default=True, verbose_name='Время работы неограничено'),
        ),
    ]
