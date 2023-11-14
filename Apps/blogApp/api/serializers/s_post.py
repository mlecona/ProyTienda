""" Serializadores de Blog """

from rest_framework import serializers
from Apps.blogApp.models import Post

class PostSerializer(serializers.ModelSerializer):
    """ Clase Serializadores de Blog """
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('creado', 'update',)
