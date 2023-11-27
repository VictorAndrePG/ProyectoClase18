from django.db import models

class Curso(models.Model):
    nombre =models.CharField(max_length=40) #dato str
    camada=models.IntegerField() #dato int

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)  # dato str
    apellido = models.CharField(max_length=40)  # dato str
    email = models.EmailField()  # dato email

