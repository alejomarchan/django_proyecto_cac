from distutils.command.upload import upload
from tkinter import image_names
from anyio import TypedAttributeLookupError
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Proyecto(models.Model):
    titulo = CharField(max_length=200)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)