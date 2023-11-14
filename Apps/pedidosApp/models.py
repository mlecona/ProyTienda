""" Modelos de Pedidos """

from django.db import models
from django.db.models import F, Sum, FloatField
#from django.contrib.auth import get_user_model
from Apps.tiendaApp.models import Producto
from django.conf import settings
User = settings.AUTH_USER_MODEL

#User = get_user_model()


class Pedido(models.Model):
    """ Modelo de Pedidos """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    creado = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        """ método de total de productos """
        return self.lineapedido_set.aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        """ clase Pedidos """
        #db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):
    """ Modelo de Pedidos """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre}"

    class Meta:
        """ clase LineaPedido """
        #db_table = 'lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Linea Pedidos'
        ordering = ['id']
