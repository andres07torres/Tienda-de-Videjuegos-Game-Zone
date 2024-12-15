from django.shortcuts import render
from django.views.generic import TemplateView, ListView , CreateView , UpdateView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class home(TemplateView):
    template_name = 'index.html'

class Nosotros(ListView):
    template_name = 'nosotros.html'
    model = Empresa
    context_object_name = 'empresa'

class Agregar(CreateView):
    template_name = 'agregar_info.html'
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('nosotros')

class Actualizar(UpdateView):
    model = Empresa
    template_name = 'actualizar_info.html'
    fields = '__all__'
    success_url = reverse_lazy('nosotros')