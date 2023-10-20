from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.forms import LibroFormulario, EditarUsuarioFormulario
from inicio.models import Libro
from inicio.forms import BusquedaFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    #template = loader.get_template(r"inicio\index.html")
    #template_renderizado = template.render()
    #return HttpResponse(template_renderizado)
    
    return render(request, r"inicio\index.html")

def cuestionario(request):
    if request.method == "POST":
           libro = Libro(titulo = request.POST.get("titulo"), autor = request.POST.get("autor"), frase = request.POST.get("frase") )
           libro.save()
           return render(request, r"inicio\index.html")
    
    formulario = LibroFormulario()
    return render(request, r"inicio\cuestionario.html", {"formulario":formulario})

def editar_usuario(request, id_usuario):
    usuario_editado = Usuario.objects.get(id=id_usuario)
      
    if request.method == "POST":
           formulario = EditarUsuarioFormulario(request.POST)
           if formulario.is_valid(): 
                data = formulario.cleaned_data
                usuario_editado.nombre = data["nombre"]
                usuario_editado.email = data["email"]
                usuario_editado.comentario = data["comentario"]
                usuario_editado.save()
                return render(request, r"inicio\index.html")
    formulario = EditarUsuarioFormulario(initial={"nombre":usuario_editado.nombre, "email": usuario_editado.email, "comentario":usuario_editado.comentario})  
    return render(request, r"inicio\editar.html", {"formulario":formulario}) 

def eliminar_usuario(request, id_usuario):
    usuario_eliminado = Usuario.objects.get(id=id_usuario)
    usuario_eliminado.delete()
    return redirect("busqueda")
    
    
     

def busqueda(request):
    formulario = BusquedaFormulario(request.GET)
    if formulario.is_valid():
        nombre_data = formulario.cleaned_data.get("nombre")
        usuario_encontrado = Usuario.objects.filter(nombre__icontains = nombre_data)
    else:
        usuario_encontrado = Usuario.objects.all()
        
    formulario = BusquedaFormulario()
    return render(request, r"inicio\busqueda.html", {"formulario":formulario, "usuario_encontrado":usuario_encontrado})