
from django.contrib import admin
from django.urls import path
from inicio.views import inicio
from inicio.views import cuestionario
from inicio.views import busqueda
from inicio.views import editar_usuario, eliminar_usuario

urlpatterns = [
    path('', inicio, name="inicio"),
    path("cuestionario", cuestionario, name="cuestionario"),
    path("busqueda", busqueda, name="busqueda"),
    path("<int:id_usuario>/editar", editar_usuario, name="editar"),
     path("<int:id_usuario>/eliminar", eliminar_usuario, name="eliminar")
]
