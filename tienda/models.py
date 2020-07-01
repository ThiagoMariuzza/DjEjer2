from django.db import models

# Create your models here.

class Comuna(models.Model):
    id_comuna =  models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

class Ciudad(models.Model):
    id_ciudad =  models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

class Cliente(models.Model):
    RUT = models.AutoField(primary_key=True)
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


    #def _str_(self):
    #    return "Autor: " + str(self.Codigo) + " " + str(self.Nombre)