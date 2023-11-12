""" Rutas de Blogs """

from django.urls import path
from Apps.blogApp.views import views
from rest_framework import routers
from Apps.blogApp.api import PostViewSet, CategoriaViewSet

router = routers.DefaultRouter()
router.register('api/post', PostViewSet, 'Apipost')
router.register('api/categoria', PostViewSet, 'Apicategori')

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
] + router.urls
