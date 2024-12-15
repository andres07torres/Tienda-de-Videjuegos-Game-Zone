from django.shortcuts import render
from django.views.generic import TemplateView, ListView , CreateView , UpdateView , DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
# Vista para la página principal (si la necesitas)
class IndexView(TemplateView):
    template_name = 'productos.html'

# Vista para listar productos
class ListaProductos(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'

# Vista para agregar un nuevo producto
class AgregarProducto(CreateView):
    model = Producto
    template_name = 'agregar_producto.html'
    fields = '__all__'  # Usamos todos los campos del modelo
    success_url = reverse_lazy('lista_productos')

# Vista para actualizar un producto existente
class ActualizarProducto(UpdateView):
    model = Producto
    template_name = 'actualizar_producto.html'
    fields = '__all__'  # Usamos todos los campos del modelo
    success_url = reverse_lazy('lista_productos')

# Vista para eliminar un producto
class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'confirmar_eliminar_producto.html'  # Asegúrate de crear esta plantilla
    success_url = reverse_lazy('lista_productos')