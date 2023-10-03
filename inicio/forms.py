from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length= 50)
    email = forms.CharField(max_length= 30)
    comentario = forms.CharField()

class BusquedaFormulario(forms.Form):
     nombre = forms.CharField(max_length= 50, required = False)