""" Configuración de Aplicaciones de Contacto """

from django.apps import AppConfig


class ContactoappConfig(AppConfig):
    """ Clase configuración de Contacto """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.contactoApp'
