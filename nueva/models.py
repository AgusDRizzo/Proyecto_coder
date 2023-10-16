from django.db import models

class paleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"marca: {self.marca}"

# Create your models here.
