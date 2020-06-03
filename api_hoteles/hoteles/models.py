from django.db import models

# Create your models here.

class Hotel(models.Model):
	nombre_hotel = models.CharField(max_length=100) #nombre hotel
	lugar = models.CharField(max_length=100) #ubicacion
	cant_hab = models.IntegerField() #cantidad de habitaciones
	disponibilidad = models.BooleanField() #cupo disponible
