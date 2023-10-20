from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir conraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {campo:"" for campo in fields}    
        
class EditarPerfilFormulario(UserChangeForm):
    password = None
    email = forms.EmailField(label="cambiar email")
    first_name = forms.CharField(label= "nombre", max_length=30)
    last_name = forms.CharField(label= "apellido", max_length=50)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar"]