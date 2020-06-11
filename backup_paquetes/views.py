from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Paquete
from datetime import datetime


def index(request):
    return HttpResponse("Nothing yet")

def armar_paquete(request):
	nombre = request.GET.get('nombre', "nombre");
	fecha_inicio = request.GET.get('fecha_inicio', "fecha inicio incorrecta");
	fecha_fin = request.GET.get('fecha_fin', "Fecha fin incorrecta");
	origen = request.GET.get('origen', "Origen incorrecto");
	destino = request.GET.get('destino', "Destino incorrecto");
	cantidad_p = request.GET.get('cantidad_p',5);
	vuelo_ida = request.GET.get('vuelo_ida',"Vuelo ida incorrecto");
	vuelo_vuelta = request.GET.get('vuelo_vuelta', "Vuelo vuelta incorrecto");
	hotel = request.GET.get('hotel', "Hotel incorrecto");
	excursion1 = request.GET.get('excursion1', "excursion1 incorrecto");
	excursion2 = request.GET.get('excursion2', "excursion2 incorrecto");
	excursion3 = request.GET.get('excursion3', "excursion3 incorrecto");
	precio = 1300
	
	fecha_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d')
	fecha_fin = datetime.strptime(fecha_fin,'%Y-%m-%d')

	p = Paquete(nombre=nombre, 
				precio=precio,
				cantidad_p=cantidad_p,
				fecha_inicio=fecha_inicio.date(),
				fecha_fin=fecha_fin.date(),
				ciudad_origen=origen,
				ciudad_destino=destino,
				excursion1=excursion1,
				excursion2=excursion2,
				excursion3=excursion3,
				hotel=hotel,
				vuelo_ida=vuelo_ida,
				vuelo_vuelta=vuelo_vuelta
				)
	p.save(force_insert=True)

	return JsonResponse({"ok": "ok"})

def reservar_paquete():
	return HttpResponse("Nothing yet")