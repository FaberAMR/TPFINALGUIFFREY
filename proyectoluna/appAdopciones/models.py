from email.mime import image
from django.db import models


# Create your models here.

class Pet(models.Model): 
    nombre =models.CharField(max_length=40) #Titulo
    fecha_nac=models.DateTimeField() #fecha
    datos=models.CharField(max_length=40) #subtutlo
    imagen=models.ImageField(upload_to='appAdopciones') #imagen
    # contacto=models.EmailField() #autor
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

