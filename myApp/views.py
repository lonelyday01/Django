from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s </h2>" % username)


def about(request):
    return render(request, "about.html")

def index(request):
    return render(request, "index.html")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, nombre):
    task = get_object_or_404(Task, title=nombre)
    return HttpResponse("tasks: %s " % task.title)

