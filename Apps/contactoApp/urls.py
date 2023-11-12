""" Rutas de Aplicación Contacto """

from django.urls import path
from Apps.contactoApp.views import views

urlpatterns = [
   path('', views.contacto, name="Contacto"),
]
