from distutils.command.upload import upload
from tkinter import image_names
from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog/image')
    fecha = models.DateField(datetime.datetime.today)