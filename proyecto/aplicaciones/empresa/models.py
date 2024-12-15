from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=255, blank=False, null=False)
    mision = models.TextField(blank=False, null=False)
    vision = models.TextField(blank=False, null=False)
    year_fundacion = models.IntegerField(blank=False, null=False)  # Año de fundación
    ruc = models.CharField(max_length=13, unique=True, blank=False, null=False)
    imagen = models.ImageField(upload_to='empresas/', blank=False, null=False)