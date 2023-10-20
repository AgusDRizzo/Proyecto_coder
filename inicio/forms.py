from django import forms
from ckeditor.fields import RichTextField 

class LibroFormulario(forms.Form):
    titulo = forms.CharField(max_length= 50)
    autor = forms.CharField(max_length= 30)
    frase = RichTextField()
    fecha = forms.DateField()

class BusquedaFormulario(forms.Form):
     titulo = forms.CharField(max_length= 50, required = False)

