""" API de Blog """

from Apps.blogApp.models import Categoria, Post
from rest_framework import viewsets, permissions
from Apps.blogApp.serializers.s_post import PostSerializer
from Apps.blogApp.serializers.s_categoria import CategoriaSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer