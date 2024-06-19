from django.db import models

# Create your models here.

class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, null=True, blank=True)

class Imagenes (models.Model):
    id_imagen = models.AutoField(primary_key=True)
    Imagenes = models.ImageField(upload_to='imagenes/')

class Producto (models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)