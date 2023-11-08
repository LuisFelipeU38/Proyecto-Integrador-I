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
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

class Jugador(CustomUser):
    CATEGORIAS = (
        ('Infantil', 'Infantil'),
        ('Juvenil', 'Juvenil'),
        ('Profesional', 'Profesional'),
    )
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # Peso en kilogramos
    estatura = models.DecimalField(max_digits=4, decimal_places=2)  # Estatura en metros
    fecha_nacimiento = models.DateField()
    posicion = models.CharField(max_length=50)

    def __str__(self):
        return self.username  # Puedes mostrar el nombre de usuario como representación del jugador

