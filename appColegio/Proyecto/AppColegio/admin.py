from django.contrib import admin

# Register your models here.
from .models import Curso, Entregable, Profesor, Estudiante


admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Curso)