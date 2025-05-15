from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('codigo_identificacion', 'especie', 'sexo', 'finca', 'municipio', 'región', 'fecha_nacimiento')
    list_filter = ('especie', 'sexo', 'municipio', 'región')
    search_fields = ('codigo_identificacion', 'finca', 'municipio', 'región')
    ordering = ('codigo_identificacion',)
