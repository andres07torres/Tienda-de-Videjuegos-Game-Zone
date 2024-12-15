from django.db import models
from aplicaciones.productos.models import Producto  # Importar Producto

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    cedula = models.CharField(max_length=10, unique=True, blank=False, null=False)
    correo = models.EmailField(blank=False, null=False)
    direccion = models.CharField(max_length=255, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    productos = models.ManyToManyField(Producto, blank=True)  # Relación directa muchos a muchos con Producto
