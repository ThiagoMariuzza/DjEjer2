from django.contrib import admin
from tienda.models import Comuna
from tienda.models import *

class ProductoInline(admin.TabularInline):
    model = Producto

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

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('RUT_P','Nombre','Web')
    list_display_links = ('RUT_P','Nombre','Web')
    list_filter = ('Nombre','RUT_P')
    search_fields = ['Nombre','RUT_P']
    inlines = [ProductoInline,]

class VentaAdmin(admin.ModelAdmin):
    list_display = ('Fecha','Descuento','RUT_C')

    actions = ['valDesc',]

    def valDesc(self,request,queryset):
        return queryset.update(Descuento = True)
    valDesc.short_description = "Validar Descuento"


# Register your models here.

admin.site.register(Comuna, )
admin.site.register(Ciudad, )
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, )
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Ventas, VentaAdmin)
admin.site.register(Detelles_Venta, )