from django.contrib import admin
from django.urls import path
from AppColegio.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="about"),
       
    
    # path('cursoformulario/', cursoFormulario, name="CursoFormulario"),
    path('listaCursos/', CursoList.as_view(), name="ListaCursos"),
    path('detalleCurso/<pk>/', CursoDetail.as_view(), name="DetalleCurso"),
    path('editarCurso/<pk>/', CursoUpdate.as_view(), name="EditarCurso"),
    path('crearCurso/', CursoCreate.as_view(), name="CrearCurso"),
    path('eliminarCurso/<pk>/', CursoDelete.as_view(), name="EliminarCurso"),
    
    # path('entregableformulario/', entregableFormulario, name="EntregableFormulario"),
    path('listaEntregables/', EntregableList.as_view(), name="ListaEntregables"),
    path('detalleEntregable/<pk>/', EntregableDetail.as_view(), name="DetalleEntregable"),
    path('editarEntregable/<pk>/', EntregableUpdate.as_view(), name="EditarEntregable"),
    path('crearEntregable/', EntregableCreate.as_view(), name="CrearEntregable"),
    path('eliminarEntregable/<pk>/', EntregableDelete.as_view(), name="EliminarEntregable"),
    
    # path('profesorformulario/', profesorFormulario, name="ProfesorFormulario"),
    path('listaProfesores/', ProfesorList.as_view(), name="ListaProfesores"),
    path('detalleProfesor/<pk>/', ProfesorDetail.as_view(), name="DetalleProfesor"),
    path('editarProfesor/<pk>/', ProfesorUpdate.as_view(), name="EditarProfesor"),
    path('crearProfesor/', ProfesorCreate.as_view(), name="CrearProfesor"),
    path('eliminarProfesor/<pk>/', ProfesorDelete.as_view(), name="EliminarProfesor"),
   
    # path('estudianteformulario/', estudianteFormulario, name="EstudianteFormulario"),
    path('listaEstudiantes/', EstudianteList.as_view(), name="ListaEstudiantes"),
    path('detalleEstudiante/<pk>/', EstudianteDetail.as_view(), name="DetalleEstudiante"),
    path('editarEstudiante/<pk>/', EstudianteUpdate.as_view(), name="EditarEstudiante"),
    path('crearEstudiante/', EstudianteCreate.as_view(), name="CrearEstudiante"),
    path('eliminarEstudiante/<pk>/', EstudianteDelete.as_view(), name="EliminarEstudiante"),
      

    path("busquedaComision", busquedaComision, name="BusquedaComision"),
    path('buscar/', buscar, name="Buscar"),
    
    path('login/', user_login, name="Login"),
    path('signup/', user_signup, name="Signup"),
    path('logout/', user_logout, name="Logout")   
]
