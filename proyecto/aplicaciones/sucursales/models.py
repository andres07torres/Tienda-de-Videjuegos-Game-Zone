from django.db import models

# Create your models here.
class Sucursal(models.Model):
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=255, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    imagen = models.ImageField(upload_to='sucursales/', blank=False, null=False)