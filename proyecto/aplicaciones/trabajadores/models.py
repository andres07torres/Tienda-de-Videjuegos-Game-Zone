from django.db import models
from aplicaciones.empresa.models import Empresa

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    correo = models.EmailField(blank=False, null=False)
    tipo_trabajador = models.CharField(max_length=20, choices=[
        ('tiempo_completo', 'Tiempo Completo'), 
        ('medio_tiempo', 'Medio Tiempo'), 
        ('fin_semana', 'Fin de Semana')
    ], blank=False, null=False)
    cedula = models.CharField(max_length=10, unique=True, blank=False, null=False)
    codigo_empleado = models.CharField(max_length=10, unique=True, blank=False, null=False)
    imagen = models.ImageField(upload_to='trabajadores/', blank=False, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con Empresa