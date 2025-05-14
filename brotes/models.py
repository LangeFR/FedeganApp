from django.db import models

class Brote(models.Model):
    ESPECIE_CHOICES = (
        ('bovino', 'Bovino'),
        ('porcino', 'Porcino'),
    )

    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    municipio = models.CharField(max_length=100)
    fecha = models.DateField()
    severidad = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return f"{self.especie} - {self.municipio} ({self.fecha})"
