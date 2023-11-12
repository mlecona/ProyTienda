""" Control de Aplicaciones de Autentica Usuario """

from django.apps import AppConfig


class AutenticaappConfig(AppConfig):
    """ Clase de Autentica Usuario """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.autenticaApp'
