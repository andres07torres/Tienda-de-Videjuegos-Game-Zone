from django.shortcuts import render
from django.views.generic import TemplateView, ListView , CreateView , UpdateView , DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'proveedores.html'
    
class ListaProveedores(ListView):
    model = Proveedor
    template_name = 'proveedores.html'
    context_object_name = 'proveedores'
    
class AgregarProveedor(CreateView):
    model = Proveedor
    template_name = 'agregar_proveedor.html'
    fields = '__all__'  # Incluir todos los campos del modelo
    success_url = reverse_lazy('lista_proveedores')
    
class ActualizarProveedor(UpdateView):
    model = Proveedor
    template_name = 'actualizar_proveedor.html'
    fields = '__all__'  # Incluir todos los campos del modelo
    success_url = reverse_lazy('lista_proveedores')
    
class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'eliminar_proveedor.html'  # Solo si tienes un archivo HTML para confirmación
    success_url = reverse_lazy('lista_proveedores')