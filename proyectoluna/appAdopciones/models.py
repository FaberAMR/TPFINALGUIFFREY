from email.mime import image
from tabnanny import verbose
from django.db import models


# Create your models here.

class Pet(models.Model): 
    nombre =models.CharField(max_length=40) #Titulo
    fecha_nac=models.DateTimeField() #fecha
    datos=models.CharField(max_length=40) #subtutlo
    imagen=models.ImageField(upload_to='appAdopciones') #imagen
    #contacto=models.IntegerField() #autor
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Adopcion'
        verbose_name_plural='Adopciones'
    
    def __str__(self):
        return self.nombre

