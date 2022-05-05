from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import Articulos
from django.conf import settings
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje = "Artículo buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]
        if len(producto)> 20:
            mensaje="Texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query":producto})
        
    else:
        mensaje="No has introducido nada"
        
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        miFormulario = FormularioContacto(request.POST)
        
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),['peredirtbike@gmail.com'],)
            
            return render(request, "gracias.html")
    else:
        miFormulario=FormularioContacto()
        
    return render(request, "formulario_contacto.html", {"form":miFormulario})
"""
        subject = request.POST['asunto']
        message = request.POST['mensaje'] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['peredirtbike@gmail.com']

        send_mail(subject, message, email_from, recipient_list)
        
        return render(request, "gracias.html")

    return render(request, "contacto.html")
"""
