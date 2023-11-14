""" Serializadores de Categoria """

from rest_framework import serializers
from Apps.blogApp.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    """ Clase Serializadores de Categoria """
    class Meta:
        model = Categoria
        fields = ['nombre', 'creado', 'update']
        read_only_fields = ('creado', 'update',)
