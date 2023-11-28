
from django.urls import path
from AppCoder.views import crear_curso, show_html

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
]


