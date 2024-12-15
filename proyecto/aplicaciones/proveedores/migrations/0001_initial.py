# Generated by Django 5.1.2 on 2024-10-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
                ('pais', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
    ]
