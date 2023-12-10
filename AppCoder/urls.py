
from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos, crear_curso_form, busqueda_camada, Cursolist, \
    CursoCreacion

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
    path('curso/', crear_curso_form),
    path('buscar/', busqueda_camada),
    path('cursos/listar',Cursolist.as_view(), name='CursosList'),
    path('crear',CursoCreacion.as_view(), name='CursoCreate'),

]


