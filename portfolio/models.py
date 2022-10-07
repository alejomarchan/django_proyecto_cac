from distutils.command.upload import upload
from django.db import models

"""Con estos módulos de Django hago las importaciones necesarias para los tipos
    de datos que va a contener nuestro modelo
"""
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Proyecto(models.Model):
    titulo = CharField(max_length=200)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)