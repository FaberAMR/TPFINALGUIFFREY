from django.urls import path
from appAtenciones import views

urlpatterns = [
    #path('mascota/', mascota),
    #path('dueño/', dueño),
    ##path('veterinario/', veterinario),
    #path('busquedas/', views.busqueda_mascota),
    #path('buscar_btn/', views.buscar_btn),
    #path('contacto/', views.contacto),
    path('', views.home, name="home"),
    path('Servicios', views.servicios, name="Servicios"), 
    path('Pets', views.Pets, name="Pets"),  
    path('Acercade', views.Acercade, name="acercade"),
    #path('Busqueda', views.Busqueda, name="Busqueda"),   

    

    ]
