from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appAtenciones.models import mascotas
from appAtenciones.forms import CargarMascota

# Create your views here.
def busqueda_mascota(request):
    return render(request, "busquedas_msct.html")

def buscar_btn(request):
    if request.GET["msct"]:
        #mensaje="mascota buscada: %r" %request.GET["msct"]
        
        pet=request.GET["msct"]
        if len(pet)>20:
            mensaje="El nombre de mascota ingresado es demasiado largo"
        else:
            mascota1=mascotas.objects.filter(nombre__icontains=pet)   
            return render(request, "resultados_busqueda.html", {"searchmascota":mascota1, "query":pet})
    else:
        mensaje="No has introducido ningun nombre"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html")
    return render(request, "contacto.html")
    
    
def Home(request):
    return HttpResponse("Home")

def servicios(request):
    return HttpResponse("Servicios")

def Pets(request):
    return HttpResponse("Pets")

#def Contacto(request):
#   return HttpResponse("Contacto")