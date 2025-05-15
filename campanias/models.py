from django.db import models
from animal.models import Animal
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

    id_campaña = models.ForeignKey(
        Campaña, on_delete=models.CASCADE, related_name='vacunaciones')
    id_vacunador = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'rol': 'vacunador'})
    id_animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.especie} - {self.finca} ({self.cantidad})"
