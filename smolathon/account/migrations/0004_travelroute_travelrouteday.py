# Generated by Django 4.2.6 on 2023-11-06 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_eventpost_category_alter_eventpost_subcategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='Дата начала')),
                ('to_date', models.DateField(verbose_name='Дата окончания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Туристический путь',
                'verbose_name_plural': 'Туристические пути',
            },
        ),
        migrations.CreateModel(
            name='TravelRouteDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.PositiveIntegerField(default=1, verbose_name='Номер дня')),
                ('day_type', models.TextField(choices=[('ST', 'Первый день'), ('EN', 'Последний'), ('MD', 'Промежуточный')], default='MD', max_length=10, verbose_name='Тип дня')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('events', models.ManyToManyField(to='posts.eventpost')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='account.travelroute')),
            ],
            options={
                'verbose_name': 'Туристический день',
                'verbose_name_plural': 'Туристические дни',
            },
        ),
    ]
