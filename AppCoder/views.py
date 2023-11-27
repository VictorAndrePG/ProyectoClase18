from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    curso = Curso(nombre="Python", camada=45) #cargo info
    curso.save() #siempre va
    return HttpResponse(f"el curso es de {curso.nombre} y la camada es {curso.camada}")