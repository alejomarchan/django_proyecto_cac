from django.contrib import admin
from .models import Categoria

# Register your models here.

#Creando la clase model Admin
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoria',)}
    list_display = ('categoria','slug')


# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
