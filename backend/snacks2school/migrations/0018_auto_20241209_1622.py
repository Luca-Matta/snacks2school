# Generated by Django 3.2.25 on 2024-12-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks2school', '0017_snack_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ingrediente_images/')),
            ],
        ),
        migrations.AddField(
            model_name='snack',
            name='ingredienti',
            field=models.ManyToManyField(related_name='snacks', to='snacks2school.Ingrediente'),
        ),
    ]