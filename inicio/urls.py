
from django.contrib import admin
from django.urls import path
from inicio.views import inicio
from inicio.views import cuestionario
from inicio.views import busqueda

urlpatterns = [
    path('', inicio, name="inicio"),
    path("cuestionario", cuestionario, name="cuestionario"),
    path("busqueda", busqueda, name="busqueda")
]
