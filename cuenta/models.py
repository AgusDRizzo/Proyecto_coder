from django.db import models
from django.contrib.auth.models import User


class InfoExtra(models.Model):
    USER = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    
# Create your models here.
