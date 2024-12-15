from django.shortcuts import render
from django.views.generic import TemplateView ,ListView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class HomePage(TemplateView):
    template_name = 'trabajadores.html'

class ListaTrabajadores(ListView):
    model = Trabajador
    template_name = 'trabajadores.html'
    context_object_name = 'trabajadores'

class AgregarTrabajador(CreateView):
    model = Trabajador
    fields = "__all__"
    template_name = 'agregar_trabajador.html'
    success_url = reverse_lazy('lista_trabajadores')

class ActualizarTrabajador(UpdateView):
    model = Trabajador
    fields = "__all__"
    template_name = 'actualizar_trabajador.html'
    success_url = reverse_lazy('lista_trabajadores')

class EliminarTrabajador(DeleteView):
    model = Trabajador
    template_name = 'trabajadors.html'
    success_url = reverse_lazy('lista_trabajadores')