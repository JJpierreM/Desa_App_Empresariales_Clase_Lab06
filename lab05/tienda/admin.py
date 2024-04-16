from django.contrib import admin

from django.contrib import admin
from django.utils.html import format_html
from .models import categoria, producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'modificar_producto')

    def modificar_producto(self, obj):
        return format_html('<a href="/admin/tienda/producto/{}/change/">Modificar</a>', obj.id)
    modificar_producto.short_description = 'Modificar Producto'

admin.site.register(categoria)
admin.site.register(producto, ProductoAdmin)

