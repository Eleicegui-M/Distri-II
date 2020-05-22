from django.db import models


class Paquete(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    
    aero_ida = models.CharField(max_length=100) #nombre aerolinea ida
    aero_vuelta = models.CharField(max_length=100) #nombre aerolinea vuelta
    vuelo_ida = models.CharField(max_length=100) #codigo de vuelo
    vuelo_vuelta = models.CharField(max_length=100) #codigo de vuelo
    fecha_ida = models.DateTimeField() #fecha-hora vuelo ida
    fecha_vuelta = models.DateTimeField() #fecha-hora vuelo vuelta


    hotel = models.CharField(max_length=100) #codigo de reserva
    hotel_noches = models.PositiveSmallIntegerField() #numero de noches
    hotel_num = models.IntegerField(default=0) #numero de habitacion

    excur_1 = models.CharField(max_length=100) # nombre excursion 1
    excur_2 = models.CharField(max_length=100) # nombre excursion 2
    excur_3 = models.CharField(max_length=100) # nombre excursion 3

    
