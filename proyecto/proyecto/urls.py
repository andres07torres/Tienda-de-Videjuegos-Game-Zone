"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.empresa.views import *
from aplicaciones.clientes.views import *
from aplicaciones.trabajadores.views import *
from aplicaciones.productos.views import *
from aplicaciones.proveedores.views import *
from aplicaciones.sucursales.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view()),
    path('empresa/', Nosotros.as_view(), name='nosotros'),
    path('agregar-info/', Agregar.as_view(), name='agregar-info'),
    path('actualizar-info/<int:pk>/', Actualizar.as_view(), name='actualizar-info'),
    path('clientes/', ListaClientes.as_view(), name='clientes'),
    path('crear-clientes/', Agregar_Cliente.as_view(), name='crear_cliente'),
    path('editar-clientes/<int:pk>/', Actualizar_Cliente.as_view(), name='editar_cliente'),
    path('eliminar-clientes/<int:pk>/', Eliminar_Cliente.as_view(), name='eliminar_cliente'),
    path('trabajadores/', ListaTrabajadores.as_view(), name='lista_trabajadores'),
    path('crear-trabajadores/', AgregarTrabajador.as_view(), name='agregar_trabajador'),
    path('actualizar-trabajadores/<int:pk>/', ActualizarTrabajador.as_view(), name='actualizar_trabajador'),
    path('eliminar-trabajador/<int:pk>/', EliminarTrabajador.as_view(), name='eliminar_trabajador'),
    path('productos/', ListaProductos.as_view(), name='lista_productos'),
    path('crear-producto/', AgregarProducto.as_view(), name='agregar_producto'),
    path('actualizar-producto/<int:pk>/', ActualizarProducto.as_view(), name='actualizar_producto'),
    path('eliminar-producto/<int:pk>/', EliminarProducto.as_view(), name='eliminar_producto'),
    path('proveedores/', ListaProveedores.as_view(), name='lista_proveedores'),
    path('agregar-proveedor/', AgregarProveedor.as_view(), name='agregar_proveedor'),
    path('actualizar-proveedor/<int:pk>/', ActualizarProveedor.as_view(), name='actualizar_proveedor'),
    path('eliminar-proveedor/<int:pk>/', EliminarProveedor.as_view(), name='eliminar_proveedor'),
    path('sucursales/', ListaSucursales.as_view(), name='lista_sucursales'),
    path('agregar-sucursal/', AgregarSucursal.as_view(), name='agregar_sucursal'),
    path('actualizar-sucursal/<int:pk>/', ActualizarSucursal.as_view(), name='actualizar_sucursal'),
    path('eliminar-sucursal/<int:pk>/', EliminarSucursal.as_view(), name='eliminar_sucursal'),
]


if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)