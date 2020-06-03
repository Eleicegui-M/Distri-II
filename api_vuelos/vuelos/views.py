from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def listar_vuelo():
	fecha_ida = request.GET['fecha_inicio']
	destino = request.GET['destino']

	array_vuelos = {}

	lista_vuelo = Vuelo.objects.filter(fecha=fecha_ida,destino=destino)

	for vuelo in lista_vuelo:
		if vuelo.disponibilidad = True:
			array_vuelos.append(vuelo)


	return JsonResponse({"vuelos": array_vuelos})

def reservar_vuelo():
	return HttpResponse("Nothing yet")