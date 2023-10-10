from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.forms import UsuarioFormulario
from inicio.models import Usuario
from inicio.forms import BusquedaFormulario
# Create your views here.

def inicio(request):
    #template = loader.get_template(r"inicio\index.html")
    #template_renderizado = template.render()
    #return HttpResponse(template_renderizado)
    
    return render(request, r"inicio\index.html")

def cuestionario(request):
    if request.method == "POST":
           usuario = Usuario(nombre = request.POST.get("nombre"), email = request.POST.get("email"), comentario = request.POST.get("comentario") )
           usuario.save()
           return render(request, r"inicio\index.html")
    
    formulario = UsuarioFormulario()
    return render(request, r"inicio\cuestionario.html", {"formulario":formulario})

def busqueda(request):
    formulario = BusquedaFormulario(request.GET)
    if formulario.is_valid():
        nombre_data = formulario.cleaned_data.get("nombre")
        usuario_encontrado = Usuario.objects.filter(nombre__icontains = nombre_data)
    else:
        usuario_encontrado = Usuario.objects.all()
        
    formulario = BusquedaFormulario()
    return render(request, r"inicio\busqueda.html", {"formulario":formulario, "usuario_encontrado":usuario_encontrado})