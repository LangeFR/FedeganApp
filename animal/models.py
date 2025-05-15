from django.db import models


class Animal(models.Model):
    ESPECIE_CHOICES = (
        ('bovino', 'Bovino'),
        ('porcino', 'Porcino'),
    )

    SEXO_CHOICES = (
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    )

    codigo_identificacion = models.CharField(max_length=50, unique=True)
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    finca = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    región = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo_identificacion} - {self.especie}"
