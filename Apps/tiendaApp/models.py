""" Modelos de Tienda """

from django.db import models


class CategoriaProd(models.Model):
    """ Clase de Categorias de Productos """
    nombre = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Clase opción Categorias """
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'

    def __str__(self):
        return str(self.nombre)


class Producto(models.Model):
    """ Clase de Productos """
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    # Para guardar archivo en carpeta media
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Clase opción Productos """
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
