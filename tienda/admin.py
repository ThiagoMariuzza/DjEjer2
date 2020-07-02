from django.contrib import admin
from tienda.models import Comuna
from tienda.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['RUT_C', 'Nombre', 'Telefono']

class ProductoAdmin(admin.ModelAdmin):
    fieldsets = ( 
        ('Descripción', {
            'fields': ('Nombre',)#no me permite id_producto
        }),
        ('Variables',{
            'fields': ('Precio','Stock')
        }),
    )

# Register your models here.

admin.site.register(Comuna, )
admin.site.register(Ciudad, )
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, )
admin.site.register(Proveedor, )
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Ventas, )