from django.db import models

"""Con estos módulos de Django hago las importaciones necesarias para los tipos
    de datos que va a contener nuestro modelo
"""
from django.db.models.fields import CharField, EmailField, IntegerField

# Create your models here.
class Integrante(models.Model):
    nombre = CharField(max_length=200)
    dni = IntegerField()
    email = EmailField(max_length = 254)