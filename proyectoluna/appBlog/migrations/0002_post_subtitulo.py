# Generated by Django 3.2.13 on 2022-05-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
