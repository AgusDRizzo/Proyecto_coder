from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from nueva.models import paleta
from django.urls import reverse_lazy

class PaletaCreateView(CreateView):
    model = paleta
    template_name = "nueva/crear_paleta.html"
    fields = ["marca", "modelo"]
    success_url = reverse_lazy("paleta_listar")


class PaletaDeleteView(DeleteView):
        model = paleta
        template_name = "nueva/eliminar_paleta.html"
        success_url = reverse_lazy("paleta_listar")
        
class PaletaDetailView(DetailView):
    model = paleta
    template_name = "nueva/detalle_paleta.html"
    
class PaletaUpdateView(UpdateView):
    model = paleta
    template_name = "nueva/editar_paleta.html"
    fields = ["marca", "modelo"]
    success_url = reverse_lazy("paleta_listar")

class PaletaListView(ListView):
    model = paleta
    context_object_name = "listado_paletas"
    template_name = "nueva/listar_paletas.html"
    



    

# Create your views here.
