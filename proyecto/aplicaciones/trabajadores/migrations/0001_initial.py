# Generated by Django 5.1.2 on 2024-10-16 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_trabajador', models.CharField(choices=[('tiempo_completo', 'Tiempo Completo'), ('medio_tiempo', 'Medio Tiempo'), ('fin_semana', 'Fin de Semana')], max_length=20)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('codigo_empleado', models.CharField(max_length=10, unique=True)),
                ('imagen', models.ImageField(upload_to='trabajadores/')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
            ],
        ),
    ]
