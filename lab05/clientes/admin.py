from django.contrib import admin

# Register your models here.

from .models import Cliente

@admin.register (Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion')

