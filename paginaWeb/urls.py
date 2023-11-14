"""
URL configuration for paginaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('Apps.userApp.api.urls')),
    path('servicios/', include('Apps.serviciosApp.urls')),
    path('blog/', include('Apps.blogApp.urls')),
    path('contacto/', include('Apps.contactoApp.urls')),
    path('tienda/', include('Apps.tiendaApp.urls')),
    path('carro/', include('Apps.carroApp.urls')),
    path('autentica/', include('Apps.autenticaApp.urls')),
    path('pedidos/', include('Apps.pedidosApp.urls')),
    path('', include('Apps.pywebApp.urls')),
]
