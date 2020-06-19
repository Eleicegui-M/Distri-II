from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Paquete
from datetime import datetime
# import requests



def index(request):
    return HttpResponse("Nothing yet")

def armar_paquete(request):
	nombre = request.GET.get('nombre', "nombre")
	fecha_inicio = request.GET.get('fecha_inicio', "0000-00-00")
	fecha_fin = request.GET.get('fecha_fin', "0000-00-00")
	origen = request.GET.get('origen', "Origen incorrecto")
	destino = request.GET.get('destino', "Destino incorrecto")
	cantidad_p = request.GET.get('cantidad_p',5)
	vuelo_ida = request.GET.get('vuelo_ida',"Vuelo ida incorrecto")
	vuelo_vuelta = request.GET.get('vuelo_vuelta', "Vuelo vuelta incorrecto")
	hotel = request.GET.get('hotel', "Hotel incorrecto")
	estrellas = request.GET.get('estrellas',2)
	excursion1 = request.GET.get('excursion1', "excursion1 incorrecto")
	excursion2 = request.GET.get('excursion2', "excursion2 incorrecto")
	excursion3 = request.GET.get('excursion3', "excursion3 incorrecto")
	
	precio_hotel = float(request.GET.get('precio_hotel',0))
	precio_vuelo_ida = float(request.GET.get('precio_vuelo_ida',0))
	precio_vuelo_vuelta = float(request.GET.get('precio_vuelo_vuelta', 0))
	precio_excursion1 = float(request.GET.get('precio_excursion1', 0))
	precio_excursion2 = float(request.GET.get('precio_excursion2', 0))
	precio_excursion3 = float(request.GET.get('precio_excursion3', 0))
	
	precio_total = precio_hotel + precio_vuelo_ida + precio_vuelo_vuelta + precio_excursion1 + precio_excursion2 + precio_excursion3
	
	fecha_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d')
	fecha_fin = datetime.strptime(fecha_fin,'%Y-%m-%d')

	p = Paquete(nombre=nombre, 
				precio=precio_total,
				cantidad_p=int(cantidad_p),
				fecha_inicio=fecha_inicio.date(),
				fecha_fin=fecha_fin.date(),
				ciudad_origen=origen,
				ciudad_destino=destino,
				excursion1=excursion1,
				excursion2=excursion2,
				excursion3=excursion3,
				hotel=hotel,
				estrellas=int(estrellas),
				vuelo_ida=vuelo_ida,
				vuelo_vuelta=vuelo_vuelta
				)
	p.save()


	print("Hace algo esto che?")
	return JsonResponse({"ok": "ok"})

def listar_paquete(request):
	paquetes = Paquete.objects.filter(reservado=False)
	return render(request,'../templates/reserva.html',{"paquetes": paquetes})

def reservar_paquete(request):
	id_paquete = request.GET['id_paquete']

	paquete = Paquete.objects.get(id=int(id_paquete))


	print ("Reservado: "+str(paquete.reservado))

	paquete.reservado = True
	print ("Reservado: "+str(paquete.reservado))



	paquete.save()

	# pload = {'hotel_id':'paquete.hotel','cant_p':'123'}
	# r = requests.post('https://httpbin.org/post',data = pload)

	# pload = {'username':'olivia','password':'123'}
	# r = requests.post('https://httpbin.org/post',data = pload)

	# pload = {'username':'olivia','password':'123'}
	# r = requests.post('https://httpbin.org/post',data = pload)

	return JsonResponse({"ok": "ok"})

