""" Modelos de Servicios """
from django.db import models

class Servicios(models.Model):
    """ Clase de Servicios """
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') # Para guardar archivo en carpeta media
    creado  = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Clase opcion servicios """
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return str(self.titulo)
