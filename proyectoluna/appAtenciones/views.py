from django.shortcuts import render, HttpResponse
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

# Create your views here.

    
def home(request):
    return render(request, "appAtenciones/home.html")

def servicios(request):
    return render(request, "appAtenciones/servicios.html")



def Acercade(request):
    return render(request, "appAtenciones/acercade.html")


#def Contacto(request):
#   return HttpResponse("Contacto")