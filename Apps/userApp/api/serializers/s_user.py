""" Serializadores de Usuarios """

from rest_framework import serializers
from Apps.userApp.models import User

class UserSerializer(serializers.ModelSerializer):
    """ Clase Serializadores de Usuarios """
    class Meta:
        model = User
        fields = '__all__'
