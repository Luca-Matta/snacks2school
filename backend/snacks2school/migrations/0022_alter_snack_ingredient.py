# Generated by Django 3.2.25 on 2024-12-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0021_alter_snack_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='ingredient',
            field=models.ManyToManyField(blank=True, null=True, related_name='snacks', to='snacks2school.Ingredient'),
        ),
    ]
