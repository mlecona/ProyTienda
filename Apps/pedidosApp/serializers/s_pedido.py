""" Serializador de Pedidos """

from rest_framework import serializers
from Apps.pedidosApp.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    """ Clase de Serializador de Pedidos """
    class Meta:
        model = Pedido
        fields = "__all__"
        read_only_fields = ('creado', 'update',)
