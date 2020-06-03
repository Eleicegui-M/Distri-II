from django.db import models


class Paquete(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField() #costo 

    fecha_inicio = models.DateTimeField() #fecha-hora vuelo ida
    fecha_vuelta = models.DateTimeField() #fecha-hora vuelo vuelta

    
    excur_1 = models.CharField(max_length=100) # nombre excursion 1
    excur_2 = models.CharField(max_length=100) # nombre excursion 2
    excur_3 = models.CharField(max_length=100) # nombre excursion 3

    hotel = models.CharField(max_length=100) #nombre hotel

    vuelo_ida = models.CharField(max_length=100) #nombre aerolinea
    vuelo_vuelta = models.CharField(max_length=100) #nombre aerolinea

