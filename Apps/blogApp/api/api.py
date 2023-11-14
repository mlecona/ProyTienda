""" API de Blog """

from rest_framework.views import APIView
from rest_framework.response import Response
# Modelos
from Apps.blogApp.models import Categoria, Post
# Serializadores
from Apps.blogApp.api.serializers.s_post import PostSerializer
from Apps.blogApp.api.serializers.s_categoria import CategoriaSerializer

class PostAPIView(APIView):
    
    def get(self, request):
        post = Post.objects.all()
        post_serializer = PostSerializer(post, many=True)
        return Response(post_serializer.data)


class CategoriaAPIView(APIView):
    
    def get(self, request):
        categoria = Categoria.objects.all()
        categoria_serializer = CategoriaSerializer(categoria, many=True)
        return Response(categoria_serializer.data)
    