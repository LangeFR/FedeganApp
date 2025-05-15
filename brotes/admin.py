from django.contrib import admin
from .models import Brote

@admin.register(Brote)
class BroteAdmin(admin.ModelAdmin):
    list_display = ('especie', 'municipio', 'fecha', 'severidad')
    list_filter = ('especie', 'municipio', 'severidad')
    search_fields = ('municipio', 'descripción')
    ordering = ('-fecha',)
