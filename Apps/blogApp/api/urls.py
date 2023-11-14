""" Rutas de Blog """

from django.urls import path
from Apps.blogApp.api.api import PostAPIView, CategoriaAPIView

urlpatterns = [
    path('post/', PostAPIView.as_view(), name="post_api"),
    path('categoria/', CategoriaAPIView.as_view(), name="categoria_api"),
]