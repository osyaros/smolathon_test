# Generated by Django 4.2.6 on 2023-10-26 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardPointTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0, editable=False, verbose_name='Вознаграждение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('check_in_url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.checkinurl')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
