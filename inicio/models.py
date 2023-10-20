from django.db import models
from ckeditor.fields import RichTextField



    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor =  models.CharField(max_length=30)
    frase = RichTextField()
    fecha = models.DateField(auto_now=True)
    imagen = models.ImageField(upload_to="libros", null=True, blank=True)
                                 
    def __str__(self):
        return f" {self.frase}\n {self.titulo} de {self.autor}\n || Publicado:{self.fecha} por "
    
# Create your models here 