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
python manage shell - abrir shell de django
https://docs.djangoproject.com/en/5.0/ref/databases/

>>> p = Project(name="Aplicacion movil") 
>>> p
<Project: Project object (None)>
>>> p.save()
>>> p = Project(name="Aplicacion web usando Django") 
>>> p.save()
>>> Project.objects.all()
<QuerySet [<Project: Project object (1)>, <Project: Project object (2)>]>
>>>>>> Project.objects.get(id=1) 
<Project: Project object (1)>
>>> Project.objects.get(id=2) 
<Project: Project object (2)>
>>> Project.objects.get(name="Aplicacion movil") 
<Project: Project object (1)>
>>> t = Task.objects
>>> t.filter(title__startswith="") 
<QuerySet [<Task: Task object (1)>, <Task: Task object (2)>]>
>>> t.all()         
<QuerySet [<Task: Task object (1)>, <Task: Task object (2)>]>
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myApp.urls"))
]
