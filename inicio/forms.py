from django import forms
from ckeditor.fields import RichTextField 

class LibroFormulario(forms.Form):
    titulo = forms.CharField(max_length= 50)
    autor = forms.CharField(max_length= 30)
    frase = RichTextField()

class BusquedaFormulario(forms.Form):
     nombre = forms.CharField(max_length= 50, required = False)

class EditarUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length= 50)
    email = forms.CharField(max_length= 30)
    comentario = forms.CharField()