from django.contrib import admin
from .models import Campaña, Vacunacion

@admin.register(Campaña)
class CampañaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)
    ordering = ('-fecha_inicio',)

@admin.register(Vacunacion)
class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('id_campaña', 'id_animal', 'id_vacunador', 'fecha')
    list_filter = ('id_campaña', 'fecha')
    search_fields = ('id_animal__codigo_identificacion', 'id_vacunador__email')
    ordering = ('-fecha',)
