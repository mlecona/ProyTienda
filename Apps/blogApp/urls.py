""" Rutas de Blogs """

from django.urls import path, include
from Apps.blogApp.views import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('api/', include('Apps.blogApp.api.urls')),
] 
