from django.contrib import admin

from proyectoluna.models import mascota, duenio, veterinario, atencion
from appAtenciones.models import mascotas, duenios, veterinarios, atenciones

class dueniosAdmin(admin.ModelAdmin):
    list_display=("nombre_apellido", "telefono")
    search_fields=("nombre_apellido","dni")

class veterinariosAdmin(admin.ModelAdmin):
    list_display=("nombre_apellido", "telefono")
    search_fields=("nombre_apellido","dni")

class atencionesAdmin(admin.ModelAdmin):
    list_display=("descripcion", "fecha_nac")
    list_filter=("fecha_nac",)
    date_hierarchy="fecha_nac"

class mascotasAdmin(admin.ModelAdmin):
    list_filter=("tipo",)


admin.site.register(duenios, dueniosAdmin)
admin.site.register(veterinarios, veterinariosAdmin)
admin.site.register(atenciones, atencionesAdmin)
admin.site.register(mascotas, mascotasAdmin)




# Register your models here.
