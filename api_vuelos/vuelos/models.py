from django.db import models

# Create your models here.

class Vuelo(models.Model):
	id_vuelo = models.CharField(max_length=100)
	nombre_aerolinea = models.CharField(max_length=100) #nombre aerolinea 
	fecha = models.DateField() #fecha-hora vuelo
	disponibilidad = models.IntegerField() #cupo disponible
	ciudad_origen = models.CharField(max_length=100) #ubicacion
	ciudad_destino = models.CharField(max_length=100) #ubicacion
	precio = models.FloatField() #costo
