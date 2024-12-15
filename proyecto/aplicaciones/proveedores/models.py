from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    pais = models.CharField(max_length=50, blank=False, null=False)
    correo = models.EmailField(blank=False, null=False)
    direccion = models.CharField(max_length=255, blank=False, null=False)