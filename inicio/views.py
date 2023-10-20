
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from inicio.models import Libro
from django.urls import reverse_lazy

def inicio(request):
    #template = loader.get_template(r"inicio\index.html")
    #template_renderizado = template.render()
    #return HttpResponse(template_renderizado)
    
    return render(request, r"inicio\index.html")

def portada(request):
    return render(request, r"inicio\portada.html")


class LibroCreateView(CreateView):
    model = Libro
    template_name = "inicio/cuestionario.html"
    fields = ["titulo", "autor", "frase"]
    success_url = reverse_lazy("inicio")


#class PaletaDeleteView(DeleteView):
 #       model = paleta
  #      template_name = "nueva/eliminar_paleta.html"
   #     success_url = reverse_lazy("paleta_listar")
    #    
#class PaletaDetailView(DetailView):
 #   model = paleta
  #  template_name = "nueva/detalle_paleta.html"