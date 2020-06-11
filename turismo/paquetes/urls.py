from django.urls import path

from . import views

urlpatterns = [
    path('armar_paquete', views.armar_paquete, name='armar_paquete'),
]