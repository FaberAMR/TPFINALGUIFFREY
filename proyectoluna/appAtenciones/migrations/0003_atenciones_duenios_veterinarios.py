# Generated by Django 3.2.13 on 2022-05-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAtenciones', '0002_rename_mascota_mascotas'),
    ]

    operations = [
        migrations.CreateModel(
            name='atenciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
                ('fecha_nac', models.DateTimeField()),
                ('estado', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='duenios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.IntegerField()),
                ('dni', models.IntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='veterinarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('matricula', models.IntegerField()),
            ],
        ),
    ]