""" Administración de Modelos de Blog """

from django.contrib import admin
from Apps.blogApp.models import Categoria, Post


class CategoriaAdmin(admin.ModelAdmin):
    """ Clase Administración  blog """
    readonly_fields = ("creado", "update")

class PostAdmin(admin.ModelAdmin):
    """ Clase Administración  blog """
    readonly_fields = ("creado", "update")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
