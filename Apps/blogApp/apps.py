""" Configuración de Aplicaciones  de blog """

from django.apps import AppConfig


class BlogappConfig(AppConfig):
    """ Clase configuración de blog """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.blogApp'
