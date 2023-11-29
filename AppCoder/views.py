from django.shortcuts import render, redirect
from AppCoder.models import Curso
from django.http import HttpResponse
from AppCoder.forms import CursoForms, BusquedaCursoForm

# Create your views here.

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto={
        "cursos":cursos,
        "form": BusquedaCursoForm(),
    }
    return render(request,'AppCoder/cursos.html', contexto)

def crear_curso(request):
    curso = Curso(nombre="Python", camada=47783)
    curso.save()

    return redirect("/app/cursos/")  # get

def crear_curso_form(request): #crearemos curso
    if request.method == "POST":
        # Crear curso
        curso_formulario = CursoForms(request.POST)
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            curso_crear = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso_crear.save()
            return redirect("/app/cursos/")

    curso_formulario = CursoForms()
    contexto = {
        "form": curso_formulario
    }
    return render(request, "AppCoder/crear_curso.html", contexto)

def busqueda_camada(request):
    nombre= request.GET["nombre"]
    cursos= Curso.objects.filter(nombre__icontains= nombre)
    contexto = {
        "cursos": cursos,
        "form": BusquedaCursoForm(),
    }
    return render(request, 'AppCoder/cursos.html', contexto)


def show_html(request):
    contexto = {"nombre":"Vic"}
    return render(request, 'index.html', contexto)

