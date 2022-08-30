from django.contrib import admin

from core.models import Categoria, Marca, Carro


admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Carro)

# Register your models here.
