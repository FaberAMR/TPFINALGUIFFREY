from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appAdopciones.models import Pet

# Create your views here.
from django.shortcuts import render

# Create your views here.

    
def home(request):
    return render(request, "appAtenciones/home.html")

def servicios(request):
    return render(request, "appAtenciones/servicios.html")

def Pets(request):
    pets=Pet.objects.all()
    return render(request, "appAtenciones/pets.html", {"pets": pets})

def Acercade(request):
    return render(request, "appAtenciones/acercade.html")


#def Contacto(request):
#   return HttpResponse("Contacto")