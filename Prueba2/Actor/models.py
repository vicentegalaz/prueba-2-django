from django.db import models

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)
    premios = models.TextField(blank=True, null=True)
    anio_debut = models.PositiveIntegerField()

