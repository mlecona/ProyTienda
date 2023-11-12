""" Manejo de Tienda"""

from django.shortcuts import redirect  # render
from Apps.carroApp.carro import Carro
from Apps.tiendaApp.models import Producto


def agregar_producto(request, producto_id):
    """ función para agregar producto """
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Producto")


def eliminar_producto(request, producto_id):
    """ función para eliminar producto """
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Producto")


def restar_producto(request, producto_id):
    """ función para restar producto """
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_prod(producto=producto)
    return redirect("Producto")


def limpia_carro(request):
    """ función para limpiar producto """
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Producto")
