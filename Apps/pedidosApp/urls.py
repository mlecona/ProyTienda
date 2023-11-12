""" Rutas de Procesar Pedidos """

from django.urls import path
from Apps.pedidosApp.views import views

urlpatterns = [
   path('', views.procesar_pedido, name="Procesar_pedido"),
]
