from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Vuelo
from datetime import datetime

# Create your views here.

def listar_vuelo(request):
	print ("entra a vuelo")
	fecha_inicio = request.GET.get('fecha_inicio', False);
	cant_p = request.GET.get('cantidad_p',2);
	origen = request.GET.get('origen', False);
	destino = request.GET.get('destino', False);

	array_vuelos = []
	array_precios = []

	fecha_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d')

	lista_vuelos = Vuelo.objects.filter(ciudad_origen=origen)

	for vuelo in lista_vuelos:
		if vuelo.ciudad_destino == destino:
			if  fecha_inicio.date() == vuelo.fecha:
				if int(cant_p) <= vuelo.disponibilidad:
					array_vuelos.append(vuelo.nombre_aerolinea)
					array_precios.append(vuelo.precio)
	print ("a ver que sale de aca: " + str(array_vuelos))

	return JsonResponse({"vuelos": array_vuelos, "precios": array_precios})

def reservar_vuelo():
	return HttpResponse("Nothing yet")