# Generated by Django 3.2.25 on 2024-12-11 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0033_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='intended_date',
        ),
        migrations.AddField(
            model_name='order',
            name='calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='snacks2school.calendar'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]