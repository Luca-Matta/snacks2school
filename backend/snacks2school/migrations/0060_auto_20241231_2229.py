# Generated by Django 3.2.25 on 2024-12-31 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0059_schoolstaff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='associated_school',
        ),
        migrations.AddField(
            model_name='user',
            name='associated_schools',
            field=models.ManyToManyField(related_name='users', to='snacks2school.School'),
        ),
        migrations.DeleteModel(
            name='SchoolStaff',
        ),
    ]
