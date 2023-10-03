from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    #template = loader.get_template(r"inicio\index.html")
    #template_renderizado = template.render()
    #return HttpResponse(template_renderizado)
    
    return render(request, r"inicio\index.html")
def cuestionario(request):
    return render(request, r"inicio\cuestionario.html")