from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView ,DeleteView
from .models import *
from django.urls import reverse_lazy

class home(TemplateView):
    template_name = 'index.html'

class ListaClientes(ListView):
    model = Cliente
    template_name = 'clientes.html'
    context_object_name = 'clientes'
    
class Agregar_Cliente(CreateView):
    model = Cliente
    template_name = 'agregar_cliente.html'  
    fields = '__all__'
    success_url = reverse_lazy('clientes')

class Actualizar_Cliente(UpdateView):
    model = Cliente
    template_name = 'actualizar_cliente.html'
    fields = '__all__'
    success_url = reverse_lazy('clientes')
    
class Eliminar_Cliente(DeleteView):
    model = Cliente
    template_name = 'confirmar_eliminar_cliente.html'
    success_url = reverse_lazy('clientes')