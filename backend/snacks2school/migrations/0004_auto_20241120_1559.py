# Generated by Django 3.2.25 on 2024-11-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='store_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
