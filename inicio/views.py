
from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from inicio.models import Libro
from django.urls import reverse_lazy
from inicio.forms import BusquedaFormulario
from django.views.generic import DetailView

def inicio(request):
    #template = loader.get_template(r"inicio\index.html")
    #template_renderizado = template.render()
    #return HttpResponse(template_renderizado)
    
    return render(request, r"inicio\index.html")

def portada(request):
    return render(request, r"inicio\portada.html")

def busqueda(request):
    formulario = BusquedaFormulario(request.GET)
    if formulario.is_valid():
        titulo_data = formulario.cleaned_data.get("titulo")
        libro_encontrado = Libro.objects.filter(titulo__icontains = titulo_data)
    else:
        libro_encontrado = Libro.objects.all()
        
    formulario = BusquedaFormulario()
    return render(request, r"inicio\busqueda.html", {"formulario":formulario, "libro_encontrado":libro_encontrado})

class LibroCreateView(CreateView):
    model = Libro
    template_name = "inicio/cuestionario.html"
    fields = ["titulo", "autor", "frase"]
    success_url = reverse_lazy("inicio")
    
class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "inicio/editar_libro.html"
    fields = ["titulo", "autor", "frase"]
    success_url = reverse_lazy("busqueda")


class LibroDeleteView(DeleteView):
        model = Libro
        template_name = "inicio/eliminar_libro.html"
        success_url = reverse_lazy("busqueda")
        
class ObjetoDetailView(DetailView):
    model = Libro
    template_name = "inicio/objeto.html"
    pk_url_kwarg = "Libro_pk"
    
#class PaletaDetailView(DetailView):
 #   model = paleta
  #  template_name = "nueva/detalle_paleta.html"