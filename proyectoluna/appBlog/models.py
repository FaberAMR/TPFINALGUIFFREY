from email.mime import image
from tabnanny import verbose
import black
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model): 
    nombre =models.CharField(max_length=40) #Titulo
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre

class Post(models.Model): 
    titulo =models.CharField(max_length=40) #Titulo
    subtitulo =models.CharField(max_length=40, null=True) #subTitulo
    contenido=models.CharField(max_length=100) #cuerpo
    imagen=models.ImageField(upload_to='appBlog', null=True, blank = True) #imagen
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categotias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.titulo