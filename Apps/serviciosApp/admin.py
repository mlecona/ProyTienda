""" Administración de Modelos de Servicios """

from django.contrib import admin
from Apps.serviciosApp.models import Servicios


class ServiciosAdmin(admin.ModelAdmin):
    """ Clase Administracion  servicios """
    readonly_fields = ("creado", "update")


admin.site.register(Servicios, ServiciosAdmin)
