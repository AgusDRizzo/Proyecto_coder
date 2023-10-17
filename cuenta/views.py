from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from cuenta.forms import FormularioRegistro
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
       
# Create your views here.
