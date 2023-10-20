from django.urls import path
from cuenta.views import login, registro, editar_perfil, editar_pass, mi_perfil
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("login/", login, name = "login"),
    path("logout/",LogoutView.as_view(template_name= "cuenta/logout.html") , name = "logout"),
    path("registro/", registro, name = "registro"),
    path("perfil/editar/", editar_perfil, name = "editar_perfil"), 
    path("perfil/editar/pass", editar_pass.as_view(), name = "editar_pass"),
    path("perfil/mi_perfil", mi_perfil, name = "mi_perfil"),
    ]
