from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Hotel
from datetime import datetime

# Create your views here.

def listar_hotel(request):
	fecha_inicio = request.GET.get('fecha_inicio', False);
	fecha_fin = request.GET.get('fecha_fin', False);
	cant_p = request.GET.get('cantidad_p',2);
	destino = request.GET.get('destino', False);

	array_hoteles = []
	array_precios = []
	array_estrellas = []

	fecha_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d').date()
	fecha_fin = datetime.strptime(fecha_fin,'%Y-%m-%d').date()

	

	lista_hoteles = Hotel.objects.filter(lugar=destino)

	for hotel in lista_hoteles:
		if  (hotel.fecha_inicio <= fecha_inicio) and (fecha_fin <= hotel.fecha_fin):
			if int(cant_p) <= hotel.disponibilidad:
				array_hoteles.append(hotel.nombre_hotel)
				array_precios.append(hotel.precio)
				array_estrellas.append(hotel.estrellas)

	return JsonResponse({"hoteles": array_hoteles,"precios":array_precios ,"estrellas": array_estrellas})

def reservar_hotel():
	return HttpResponse("Nothing yet")