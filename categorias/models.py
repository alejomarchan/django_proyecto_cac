from django.db import models

from django.db.models import CharField, TextField, SlugField


# Create your models here.
class Categoria(models.Model):
    categoria = CharField(max_length=200, unique=True)
    slug         = SlugField(max_length=200, unique=True)
    descripcion  = TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.categoria
