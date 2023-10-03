from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.forms import UsuarioFormulario
from inicio.models import Usuario

# Create your views here.

def inicio(request):
    #template = loader.get_template(r"inicio\index.html")
    #template_renderizado = template.render()
    #return HttpResponse(template_renderizado)
    
    return render(request, r"inicio\index.html")

def cuestionario(request):
    if request.method == "POST":
           usuario = Usuario(nombre = request.POST.get("nombre"), email = request.POST.get("email"), comentario = request.POST.get("comentario") )
           return render(request, r"inicio\index.html")
    
    formulario = UsuarioFormulario()
    return render(request, r"inicio\cuestionario.html", {"formulario":formulario})