from django import forms

class CursoForms(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()


class BusquedaCursoForm(forms.Form):
    nombre = forms.CharField()