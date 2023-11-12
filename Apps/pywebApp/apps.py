""" Configuración de Aplicaciones  de Web """

from django.apps import AppConfig


class PywebappConfig(AppConfig):
    """ Clase configuración de Web """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.pywebApp'
