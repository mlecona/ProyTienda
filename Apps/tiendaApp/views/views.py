""" Vistas de Tienda """

from django.shortcuts import render
from Apps.tiendaApp.models import CategoriaProd, Producto

def producto(request):
    """ funcion de tienda """
    miproducto = Producto.objects.all()
    return render(request, "tienda/producto.html", {"productos": miproducto})

def categoriaprod(request):
    """ funcion de tienda """
    micategoriaprod = CategoriaProd.objects.all()
    return render(request, "tienda/categoria.html", {"categorias": micategoriaprod})
