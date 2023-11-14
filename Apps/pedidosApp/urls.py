""" Rutas para Procesar Pedidos """

from django.urls import path
from Apps.pedidosApp.views import views
from rest_framework import routers
from Apps.pedidosApp.api import PedidoViewSet, LineaPedidoViewSet

router = routers.DefaultRouter()
router.register('api/pedido', PedidoViewSet, 'Apipedido')
router.register('api/lineaped', LineaPedidoViewSet, 'Apilineped')

urlpatterns = [
   path('', views.procesar_pedido, name="Procesar_pedido"),
] + router.urls
