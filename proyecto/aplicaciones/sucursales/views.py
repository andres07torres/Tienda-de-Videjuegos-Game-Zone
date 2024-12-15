from django.shortcuts import render
from django.views.generic import TemplateView, ListView , CreateView , UpdateView ,DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class HomePage(TemplateView):
    template_name = 'sucursales.html'

class ListaSucursales(ListView):
    model = Sucursal
    template_name = 'sucursales.html'
    context_object_name = 'sucursales'

# Vista para agregar una nueva sucursal
class AgregarSucursal(CreateView):
    model = Sucursal
    template_name = 'agregar_sucursal.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_sucursales')

# Vista para actualizar una sucursal existente
class ActualizarSucursal(UpdateView):
    model = Sucursal
    template_name = 'actualizar_sucursal.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_sucursales')

# Vista para eliminar una sucursal
class EliminarSucursal(DeleteView):
    model = Sucursal
    template_name = 'confirmar_eliminar_sucursal.html'
    success_url = reverse_lazy('lista_sucursales')
