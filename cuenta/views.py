from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from cuenta.forms import FormularioRegistro, EditarPerfilFormulario
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data= request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")
            usuario = authenticate(username=username, password=password)
            django_login(request, usuario)
            return redirect("inicio")
    else:
        formulario = AuthenticationForm()
        return render (request, "cuenta/login.html", {"formulario":formulario})
def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    else:
        formulario = FormularioRegistro()
        return render(request, "cuenta/registro.html",  {"formulario":formulario})
       
def editar_perfil(request):
    
    #info_extra = request.user.infoextra
    
    if request.method == "POST":
        formulario = EditarPerfilFormulario(request.POST, instance=request.user)
        if formulario.is_valid():
               if formulario.cleaned_data.get("avatar"):
                     #info_extra.avatar = formulario.cleaned_data.get("avatar")
                     #info_extra.save()
                     formulario.save()
                     return redirect("inicio")
    else:    
        formulario = EditarPerfilFormulario(instance=request.user) #initial=
    return render(request, "cuenta/editar_perfil.html", {"formulario":formulario})

class editar_pass(PasswordChangeView):
    template_name = "cuenta/editar_pass.html"
    success_url = reverse_lazy("editar_perfil")
    
# Create your views here.
