""" Rutas de Tienda """

from django.urls import path
from Apps.carroApp.views import views
app_name = "app_carro"
urlpatterns = [
    path('agregar/<int:producto_id>', views.agregar_producto, name="Agregar"),
    path('eliminar/<int:producto_id>', views.eliminar_producto, name="Eliminar"),
    path('restar/<int:producto_id>', views.restar_producto, name="Restar"),
    path('limpiar/', views.limpia_carro, name="Limpiar"),
]
