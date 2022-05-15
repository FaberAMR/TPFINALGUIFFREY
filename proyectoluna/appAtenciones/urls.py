from django.urls import path
from appAtenciones import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('mascota/', mascota),
    #path('dueño/', dueño),
    ##path('veterinario/', veterinario),
    #path('busquedas/', views.busqueda_mascota),
    #path('buscar_btn/', views.buscar_btn),
    #path('contacto/', views.contacto),
    path('', views.home, name="home"),
    path('Servicios', views.servicios, name="Servicios"), 
    path('Acercade', views.Acercade, name="acercade"),
    #path('Busqueda', views.Busqueda, name="Busqueda"),   

    

    ]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)