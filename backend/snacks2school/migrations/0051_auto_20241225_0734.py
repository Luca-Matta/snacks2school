# Generated by Django 3.2.25 on 2024-12-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0050_auto_20241220_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='prepared',
            field=models.BooleanField(default=False),
        ),
    ]