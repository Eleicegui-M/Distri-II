from django.db import models

# Create your models here.

class Hotel(models.Model):
	nombre_hotel = models.CharField(max_length=100) #nombre hotel
	lugar = models.CharField(max_length=100) #ubicacion
	disponibilidad = models.IntegerField() #cupo disponible
	precio = models.FloatField() #costo
	fecha_inicio = models.DateTimeField() #
	fecha_fin = models.DateTimeField() #
	estrellas = models.IntegerField() #