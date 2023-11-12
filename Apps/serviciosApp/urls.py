""" Rutas de Servicios """

from django.urls import path
from Apps.serviciosApp.views import views

urlpatterns = [
    path('', views.servicios, name="Servicios"),
]
