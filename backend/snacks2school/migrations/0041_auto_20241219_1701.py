# Generated by Django 3.2.25 on 2024-12-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0040_auto_20241219_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]