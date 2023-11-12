""" Rutas de Autenticación de Usuario """

from django.urls import path
from Apps.autenticaApp.views import views

urlpatterns = [
   path('', views.Registroview.as_view(), name="Autentica"),
   path('cerrar_sesion', views.cerrar_sesion, name="Cerrar_sesion"),
   path('logear', views.logear, name="Logear"),
]
