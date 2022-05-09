from django.db import models


# Create your models here.

class mascota(models.Model): #agregar columna tipo de mascota
    nombre =models.CharField(max_length=40)
    fecha_nac=models.DateTimeField()
    tipo=models.CharField(max_length=40)
    raza=models.CharField(max_length=40)
    def __str__(self):
        return 'El nombre de la mascota es %s , es %s , la raza es %s , y nacio el %s' % (self.nombre, self.tipo, self.raza, self.fecha_nac)

class duenio(models.Model):
    nombre_apellido =models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    email=models.EmailField(blank=True, null=True)
    telefono=models.IntegerField()
    dni=models.IntegerField(verbose_name="DNI")
    def __str__(self):
        return self.nombre_apellido

class veterinario(models.Model):
    nombre_apellido =models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    email=models.EmailField()
    telefono=models.IntegerField()
    matricula=models.IntegerField()
    def __str__(self):
        return self.nombre_apellido

class atencion(models.Model):
    descripcion=models.CharField(max_length=40)
    fecha_nac=models.DateTimeField()
    estado=models.CharField(max_length=40) 
