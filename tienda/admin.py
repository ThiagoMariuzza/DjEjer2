from django.contrib import admin
from tienda.models import Comuna
from tienda.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['RUT_C', 'Nombre', 'Telefono']

# Register your models here.

admin.site.register(Comuna, )
admin.site.register(Ciudad, )
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, )
admin.site.register(Proveedor, )
admin.site.register(Producto, )
admin.site.register(Ventas, )