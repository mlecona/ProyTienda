""" Para agregar en Panel de Administración de Modelos de Tienda """

from django.contrib import admin
from Apps.tiendaApp.models import CategoriaProd, Producto


class ProductoAdmin(admin.ModelAdmin):
    """ Clase Administracion  Tienda """
    readonly_fields = ("creado", "update")


class CategoriaProdAdmin(admin.ModelAdmin):
    """ Clase Administracion  Tienda """
    readonly_fields = ("creado", "update")


admin.site.register(Producto, ProductoAdmin)
admin.site.register(CategoriaProd, CategoriaProdAdmin)
