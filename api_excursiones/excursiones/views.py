from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def listar_excursion():
	fecha_inicio = request.GET['fecha_inicio']
	fecha_fin = request.GET['fecha_fin']
	destino = request.GET['destino']

	array_excuriones = {}

	lista_excursiones = Excursion.objects.filter(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,destino=destino)

	for excursion in lista_excursiones:
		if excursion.disponibilidad = True:
			array_excursiones.append(excursion)


	return JsonResponse({"excursiones": array_excursiones})

def reservar_excursion():
	return HttpResponse("Nothing yet")