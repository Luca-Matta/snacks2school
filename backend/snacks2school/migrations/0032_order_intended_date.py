# Generated by Django 3.2.25 on 2024-12-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0031_delete_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='intended_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]