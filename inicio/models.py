from django.db import models
from ckeditor.fields import RichTextField



    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor =  models.CharField(max_length=30)
    frase = RichTextField()
    fecha = models.DateField(auto_now=True)
                                 
    def __str__(self):
        return f"Título: {self.titulo}:\n Autor:{self.autor}\n Frase: {self.frase}\n Fecha:{self.fecha}"
    
# Create your models here 