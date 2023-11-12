""" Serializadores de Categoria """

from rest_framework import serializers
from Apps.blogApp.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    """ Clase de Serializadores de Categoria """
    class Meta:
        model = Categoria
        fields = "__all__"
        read_only_fields = ('creado', 'update',)
