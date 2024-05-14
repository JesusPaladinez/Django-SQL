"""
URL configuration for GestionPeliculas project.

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
from django.urls import path
from appPeliculas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio),
    path("vistaAgregarGenero/", views.vistaAgregarGenero),
    path("agregarGenero/", views.agregarGenero),
    path("listarPeliculas/", views.listarPeliculas),
    path("vistaAgregarPeliculas/", views.vistaAgregarPeliculas),
    path("agregarPeliculas/", views.agregarPeliculas),
    path("consultarPelicula/<int:id>/", views.consultarPeliculaId),
    path('actualizarPelicula/',views.actualizarPelicula),
    path('eliminarPelicula/<int:id>/',views.eliminarPelicula),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)