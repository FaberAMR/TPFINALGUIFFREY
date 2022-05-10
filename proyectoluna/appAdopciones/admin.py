from django.contrib import admin
from .models import Pet

# Register your models here.


class petAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Pet, petAdmin)