"""
URL configuration for MySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

commands:
python manage runserver - ejecuta el sitio
python manage startapp {nombre} - crea una nueva app
python manage makemigratios - detecta las posibles migraciones
python manage migrate - realiza las migraciones
https://docs.djangoproject.com/en/5.0/ref/databases/
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cosas/", include("myApp.urls"))
]
