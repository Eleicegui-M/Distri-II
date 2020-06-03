from django.db import models

# Create your models here.

class Vuelo(models.Model):
	nombre_aerolinea = models.CharField(max_length=100) #nombre aerolinea 
	id_vuelo = models.CharField(max_length=100) #codigo de vuelo
	fecha = models.DateTimeField() #fecha-hora vuelo
	cant_pasajeros = models.IntegerField()
