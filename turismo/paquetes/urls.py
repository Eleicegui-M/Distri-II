from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('armar_paquete', views.armar_paquete, name='armar_paquete'),
    path('reservar_paquete', views.reservar_paquete, name='reservar_paquete'),
]