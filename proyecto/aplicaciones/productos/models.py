from django.db import models
from aplicaciones.sucursales.models import Sucursal  # Relación con Sucursal
from aplicaciones.proveedores.models import Proveedor  # Relación con Proveedor

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    area = models.CharField(max_length=20, choices=[
        ('puzzle', 'Puzzle'),
        ('estrategia', 'Estrategia'),
        ('aventura_logica', 'Aventura Lógica'),
        ('rpg', 'RPG'),
        ('simulacion', 'Simulación'),
        ('juegos_educativos', 'Juegos Educativos'),
        ('juegos_de_mesa', 'Juegos de Mesa'),
        ('rompecabezas', 'Rompecabezas'),
        ('juegos_interactivos', 'Juegos Interactivos'),
        ('otros', 'Otros')
    ], blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    iva = models.IntegerField(choices=[(15, '15%'), (0, '0%')], blank=False, null=False)
    imagen = models.ImageField(upload_to='productos/', blank=False, null=False)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)  # Relación con sucursal (ahora permite valores nulos)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)  # Relación con proveedor (ahora permite valores nulos)
