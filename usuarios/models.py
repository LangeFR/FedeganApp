from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('vacunador', 'Vacunador'),
    )
    username = None  # Eliminamos username
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default="vacunador")
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
