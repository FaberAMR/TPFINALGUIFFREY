# Generated by Django 3.2.13 on 2022-05-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdopciones', '0004_alter_pet_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='appAtenciones'),
        ),
    ]
