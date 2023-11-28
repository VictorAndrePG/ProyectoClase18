from django.shortcuts import render, redirect
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto={
        "cursos":cursos,
    }
    return render(request,'AppCoder/cursos.html', contexto)

def crear_curso(request):
    curso = Curso(nombre="Python", camada=47783)
    curso.save()

    return redirect("/app/cursos/")  # get

def show_html(request):
    contexto = {"nombre":"Vic"}
    return render(request, 'index.html', contexto)

