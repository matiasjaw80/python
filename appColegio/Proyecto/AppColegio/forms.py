from django import forms
from .models import Entregable, Estudiante, Curso, Profesor
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class CursoFormulario(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'comision', 'codigo', 'imagen']


class ProfesorFormulario(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']


class EntregableFormulario(ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado', 'estudiante']


class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
