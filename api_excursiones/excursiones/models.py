from django.db import models

# Create your models here.

class Excursion(models.Model):
	nombre_excursion = models.CharField(max_length=100) #nombre excursion 
	lugar = models.CharField(max_length=100) #ubicacion
	fecha = models.DateField() #fecha-hora salida
	disponibilidad = models.IntegerField() #cupo disponible
	precio = models.FloatField() #costo