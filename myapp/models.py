from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=50)
    direccion = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.nombreProducto    


class Venta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta #{self.id} - {self.cliente} - {self.producto}'
