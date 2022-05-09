"""proyectoluna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from proyectoluna.views import mascota, dueño, veterinario
#from appAtenciones.views import busqueda_mascota, buscar_btn
#from appAtenciones import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appAtenciones.urls')),
    #path('mascota/', mascota),
    #path('dueño/', dueño),
    ##path('veterinario/', veterinario),
    #path('busquedas/', views.busqueda_mascota),
    #path('buscar_btn/', views.buscar_btn),
    ##path('contacto/', views.contacto),
    #path('Home', views.Home, name="Home"),
    #path('Servicios', views.servicios, name="Servicios"), 
    #path('Pets', views.Pets, name="Pets"),  

 

    ]
