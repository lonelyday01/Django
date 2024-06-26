from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# los modelos creados seran tablas pertenecientes a la DB
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # on_delete es para cuando se eliminee un dato en cascada se eliminaran los relacionados

    def __str__(self):
        return self.title + ' - ' + self.description + ' - ' + self.project.name
    
class Action(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
