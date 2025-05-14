from django.db import models
from usuarios.models import User

class Campaña(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Vacunacion(models.Model):
    ESPECIE_CHOICES = (
        ('bovino', 'Bovino'),
        ('porcino', 'Porcino'),
    )

    campaña = models.ForeignKey(Campaña, on_delete=models.CASCADE, related_name='vacunaciones')
    vacunador = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'rol': 'vacunador'})
    finca = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    región = models.CharField(max_length=100)
    fecha = models.DateField()
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.especie} - {self.finca} ({self.cantidad})"
