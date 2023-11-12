""" Para agregar en Panel de Administración de Modelos de Pedidos """

from django.contrib import admin
from Apps.pedidosApp.models import Pedido, LineaPedido


class PedidoAdmin(admin.ModelAdmin):
    """ Clase Administración  Tienda """
    readonly_fields = ("creado", "update")


class LineaPedidoAdmin(admin.ModelAdmin):
    """ Clase Administración  Tienda """
    readonly_fields = ("creado", "update")


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)
