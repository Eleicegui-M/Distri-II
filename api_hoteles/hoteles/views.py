from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Hotel
from datetime import datetime

# Create your views here.

def listar_hotel(request):
	print("entra a hoteles")
	fecha_inicio = request.GET.get('fecha_inicio', False);
	fecha_fin = request.GET.get('fecha_fin', False);
	cant_p = request.GET.get('cantidad_p',2);
	destino = request.GET.get('destino', False);

	array_hoteles = []
	array_estrellas = []

	fecha_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d')
	fecha_fin = datetime.strptime(fecha_fin,'%Y-%m-%d')

	lista_hoteles = Hotel.objects.filter(lugar=destino)

	for hotel in lista_hoteles:
		print ("fecha inicio: "+str(hotel.fecha_inicio))
		print ("fecha fin: "+str(hotel.fecha_fin))
		if  fecha_inicio.date() <= hotel.fecha_inicio and hotel.fecha_fin <= fecha_fin.date():
			if int(cant_p) <= hotel.disponibilidad:
				array_hoteles.append(hotel.nombre_hotel)
				array_estrellas.append(hotel.estrellas)


	return JsonResponse({"hoteles": array_hoteles, "estrellas": array_estrellas})

def reservar_hotel():
	return HttpResponse("Nothing yet")