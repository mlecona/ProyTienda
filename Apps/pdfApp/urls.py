""" Rutas de Aplicación para Generar PDF """

from django.urls import path
from Apps.pdfApp.views import views

urlpatterns = [
   path('', views.contacto, name="Contacto"),
]
