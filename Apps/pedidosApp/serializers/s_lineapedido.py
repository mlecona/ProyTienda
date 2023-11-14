""" Serializador de Linea de Pedidos """

from rest_framework import serializers
from Apps.pedidosApp.models import LineaPedido


class LineaPedidoSerializer(serializers.ModelSerializer):
    """ Clase Serializador de Linea de Pedidos """
    class Meta:
        model = LineaPedido
        fields = "__all__"
        read_only_fields = ('cantidad', 'creado', 'update',)
