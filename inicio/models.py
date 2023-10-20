from django.db import models
from ckeditor.fields import RichTextField


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email =  models.CharField(max_length=30)
    comentario = models.TextField()
    
    def __str__(self):
        return f"nombre = {self.nombre}, email = {self.email}, comentario = {self.comentario}\n"
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor =  models.CharField(max_length=30)
    frase = RichTextField()
    fecha = models.DateField(auto_now=True)
                                 
    def __str__(self):
        return f"Título: {self.titulo}:\n Autor:{self.autor}\n Frase: {self.frase}\n Fecha:{self.fecha}"
    
# Create your models here 