from django.db import models


class Paquete(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(default=1200) #costo
    cantidad_p = models.IntegerField() #cant personas
    fecha_inicio = models.DateField() #fecha-hora vuelo ida
    fecha_fin = models.DateField() #fecha-hora vuelo vuelta
    ciudad_origen = models.CharField(max_length=100) #ubicacion
    ciudad_destino = models.CharField(max_length=100) #ubicacion
    excursion1 = models.CharField(max_length=100) # nombre excursion 1
    excursion2 = models.CharField(max_length=100) # nombre excursion 2
    excursion3 = models.CharField(max_length=100) # nombre excursion 3
    hotel = models.CharField(max_length=100) #nombre hotel
    vuelo_ida = models.CharField(max_length=100) #nombre aerolinea
    vuelo_vuelta = models.CharField(max_length=100) #nombre aerolinea


