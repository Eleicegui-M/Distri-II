from django.urls import path

from . import views

urlpatterns = [
    path('armar_paquete', views.armar_paquete, name='armar_paquete'),
    path('reservar_paquete', views.reservar_paquete, name='reservar_paquete'),
    path('listar_paquete', views.listar_paquete, name='listar_paquete'),

]