
from django.contrib import admin
from django.urls import path
from inicio import views
from inicio.views import inicio
from inicio.views import portada

#from inicio.views import busqueda
#from inicio.views import editar_usuario, eliminar_usuario

urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path("cuestionario", views.LibroCreateView.as_view(), name="cuestionario"),    
    path("", portada, name="portada")
    #path("busqueda", busqueda, name="busqueda"),
    #path("<int:id_usuario>/editar", editar_usuario, name="editar"),
     #path("<int:id_usuario>/eliminar", eliminar_usuario, name="eliminar")
]
