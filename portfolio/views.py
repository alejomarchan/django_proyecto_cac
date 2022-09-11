from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'home.html', {'proyectos': proyectos})