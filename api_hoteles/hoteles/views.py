from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def listar_hotel():
	fecha_inicio = request.GET['fecha_inicio']
	fecha_fin = request.GET['fecha_fin']
	destino = request.GET['destino']

	array_hoteles = {}

	lista_hotel = Hotel.objects.filter(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,destino=destino)

	for hotel in lista_hotel:
		if hotel.disponibilidad = True:
			array_hoteles.append(hotel)


	return JsonResponse({"hoteles": array_hoteles})

def reservar_hotel():
	return HttpResponse("Nothing yet")