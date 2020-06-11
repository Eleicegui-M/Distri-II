from django.shortcuts import render
from .models import Excursion
from django.http import HttpResponse,JsonResponse
from datetime import datetime

# Create your views here.

def listar_excursion(request):
	print("entra a excursion")
	fecha_inicio = request.GET.get('fecha_inicio', False);
	fecha_fin = request.GET.get('fecha_fin', False);
	cant_p = request.GET.get('cantidad_p',2);
	destino = request.GET.get('destino', False);

	array_excursiones = []
	array_precio = []

	fecha_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d')
	fecha_fin = datetime.strptime(fecha_fin,'%Y-%m-%d')

	lista_excursiones = Excursion.objects.filter(lugar=destino)

	for excursion in lista_excursiones:
		if  fecha_inicio.date() <= excursion.fecha and excursion.fecha <= fecha_fin.date():
			if int(cant_p) <= excursion.disponibilidad:
				array_excursiones.append(excursion.nombre_excursion)
				array_precio.append(excursion.precio)

	return JsonResponse({"excursiones": array_excursiones, "precios": array_precio})

def reservar_excursion():
	return HttpResponse("Nothing yet")