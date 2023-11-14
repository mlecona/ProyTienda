""" API de Blog """

from Apps.pedidosApp.models import Pedido, LineaPedido
from rest_framework import viewsets, permissions
from Apps.pedidosApp.serializers.s_pedido import PedidoSerializer
from Apps.pedidosApp.serializers.s_lineapedido import LineaPedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer

class LineaPedidoViewSet(viewsets.ModelViewSet):
    queryset = LineaPedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LineaPedidoSerializer