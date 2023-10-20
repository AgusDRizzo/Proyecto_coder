
from django.contrib import admin
from django.urls import path
from inicio import views
from inicio.views import inicio
from inicio.views import portada
from inicio.views import busqueda, quien_soy


#from inicio.views import busqueda
#from inicio.views import editar_usuario, eliminar_usuario

urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path("cuestionario", views.LibroCreateView.as_view(), name="cuestionario"),    
    path("", portada, name="portada"),
    path("busqueda", busqueda, name="busqueda"),
    path("<int:pk>/editar", views.LibroUpdateView.as_view(), name="editar_libro"),
     path("<int:pk>/eliminar", views.LibroDeleteView.as_view(), name="eliminar_libro"), 
     path("<Libro_pk>/objeto", views.ObjetoDetailView.as_view(), name="objeto" ), 
     path('quien_soy', quien_soy, name="quien_soy"),
]
