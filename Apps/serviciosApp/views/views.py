""" Vistas de Servicios """

from django.shortcuts import render
from Apps.serviciosApp.models import Servicios


def servicios(request):
    """ funcion de Servicios """
    miservicios = Servicios.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": miservicios})
