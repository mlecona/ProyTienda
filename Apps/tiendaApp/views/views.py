""" Vistas de Tienda """

from django.shortcuts import render
from Apps.tiendaApp.models import CategoriaProd, Producto

def producto(request):
    """ función de tienda """
    miproducto = Producto.objects.all()
    return render(request, "tienda/producto.html", {"productos": miproducto})

def categoriaprod(request):
    """ función de tienda """
    micategoriaprod = CategoriaProd.objects.all()
    return render(request, "tienda/categoria.html", {"categorias": micategoriaprod})
