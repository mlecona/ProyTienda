""" Rutas de Aplicación web"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Apps.pywebApp.views import views

urlpatterns = [
    path('', views.home, name="Home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

