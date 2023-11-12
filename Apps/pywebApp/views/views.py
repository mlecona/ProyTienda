""" Vistas de Pagina Web """

from django.shortcuts import render

from Apps.carroApp.carro import Carro

def home(request):
    """ Función de Inicio """
    carro = Carro(request)
    return render(request, "pywebApp/home.html")
