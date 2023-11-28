
from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
]


