# Generated by Django 3.2.13 on 2022-04-25 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoluna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duenio',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
