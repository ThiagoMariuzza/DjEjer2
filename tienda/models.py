from django.db import models

# Create your models here.

class Comuna(models.Model):
    id_comuna =  models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

class Ciudad(models.Model):
    id_ciudad =  models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

class Cliente(models.Model):
    RUT_C = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=30)
    Calle = models.CharField(max_length=30)
    Numero = models.IntegerField()
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    Comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=50)

class Proveedor(models.Model):
    RUT_P = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=30)
    Web = models.CharField(max_length=30)
    Calle = models.CharField(max_length=30)
    Numero = models.IntegerField()
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    Comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, default = None)
    Nombre = models.CharField(max_length=30)
    Precio = models.IntegerField()
    Stock = models.IntegerField()
    RUT_P = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Detelles_Venta(models.Model):
    id_detalle = models.AutoField(primary_key=True, default = None)
    cantidad = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def _str_(self):
        return "Detalles: " + str(self.id_detalle) + " " + str(self.cantidad)

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    RUT_C = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Descuento = models.IntegerField()
    id_detalle = models.ForeignKey(Detelles_Venta, on_delete=models.CASCADE, default = None)
            
    #def _str_(self):
    #    return "Autor: " + str(self.Codigo) + " " + str(self.Nombre)