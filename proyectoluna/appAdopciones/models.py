from email.mime import image
from tabnanny import verbose
import black
from django.db import models


# Create your models here.
class Tipo(models.Model): 
    nombre =models.CharField(max_length=40) 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='tipo'
        verbose_name_plural='tipos'
    
    def __str__(self):
        return self.nombre

class Pet(models.Model): 
    nombre =models.CharField(max_length=40) #Titulo
    fecha_nac=models.DateTimeField() #fecha
    datos=models.CharField(max_length=40) #subtutlo
    imagen=models.ImageField(upload_to='appAtenciones', null=True, blank = True) #imagen
    tipo=models.CharField(max_length=40, null=True)
    tipos=models.ManyToManyField(Tipo)
    #contacto=models.IntegerField() 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Pet'
        verbose_name_plural='Pets'
    
    def __str__(self):
        return self.nombre


