from django.shortcuts import render
from .models import Integrante

#Con este paquete, invoco el decorador de login_required
from django.contrib.auth.decorators import login_required


# Create your views here.
"""
Con el @login_required en esta vista, cuando algún usuario quiera acceder a ella, verifica si está logueado. Si el usuario no ha iniciado sesión lo va a redirigir a la página de login y si no está registrado, podrá hacerlo en la plantilla de registro
"""
@login_required
def integrantes(request):
    integrantes = Integrante.objects.all()
    return render(request, 'integrantes.html', {'integrantes': integrantes})