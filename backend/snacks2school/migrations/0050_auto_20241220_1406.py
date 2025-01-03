# Generated by Django 3.2.25 on 2024-12-20 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0049_alter_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='snacks2school.school'),
        ),
        migrations.AddField(
            model_name='order',
            name='school_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='snacks2school.class'),
        ),
    ]
