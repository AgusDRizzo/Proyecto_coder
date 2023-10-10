from django.db import models
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email =  models.CharField(max_length=30)
    comentario = models.TextField()
    
    def __str__(self):
        return f"nombre = {self.nombre}, email = {self.email}, comentario = {self.comentario}\n"
    
# Create your models here 