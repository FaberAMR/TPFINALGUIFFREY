from django.http import HttpResponse
import datetime
from django.template import Template, context
from django.template.loader import get_template
from django.shortcuts import render

def mascota(request):
    fecha = datetime.datetime.now()    
    return render(request, "mascota.html", {'ahora': fecha})


def saludo(request):
    fecha = datetime.datetime.now()
   
    return render(request, "index.html", {'ahora' : fecha})

def dueño(request):
    fecha = datetime.datetime.now()    
    return render(request, "dueño.html", {'ahora': fecha})

def veterinario(request):
    fecha = datetime.datetime.now()    
    return render(request, "veterinario.html", {'ahora': fecha})


