
from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos, crear_curso_form, busqueda_camada

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
    path('curso/', crear_curso_form),
    path('buscar/', busqueda_camada),
]


