from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Agregar un campo para distinguir el tipo de usuario (jugador, entrenador, administrador)
    USER_TYPE_CHOICES = (
        ('jugador', 'Jugador'),
        ('entrenador', 'Entrenador'),
        ('admin', 'Administrador'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='jugador')
