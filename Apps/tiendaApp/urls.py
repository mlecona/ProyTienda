""" Rutas de Tienda """

from django.urls import path
from Apps.tiendaApp.views import views

urlpatterns = [
    path('', views.producto, name="Producto"),
    #path('categoria/', views.categoriaprod, name="Categoriaprod"),
]
