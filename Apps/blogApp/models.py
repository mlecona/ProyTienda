""" Modelos de Blogs """

from django.db import models
from django.contrib.auth import models as auth_models


class Categoria(models.Model):
    """ Clase de Categorías """
    nombre = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Clase opción Categoria """
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return str(self.nombre)


class Post(models.Model):
    """ Clase de Post """
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # Para guardar archivo en carpeta media
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    creado = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Clase opción Post """
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return str(self.titulo)
