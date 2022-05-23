from django.conf.urls import url
from django.urls import path
from .views import registroUsuario, cerrar_sesion, loguear
#from proyectoluna.appUsuarios.views import autenticacion, registroUsuario, usuarios
#from apps.appUsuarios.views import registroUsuario 


urlpatterns = [
    #url(r'^registro', registroUsuario.as_view(), name="registro")
    path('', registroUsuario.as_view(), name="Usuarios"), 
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"), 
    path('loguear', loguear, name="loguear"),    
    ]
