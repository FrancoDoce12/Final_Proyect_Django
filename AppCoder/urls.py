from django.urls import path
from  django.contrib.auth.decorators import login_required

from AppCoder.views import crear_curso, inicio, cursos,agregar_avatar, profesores,estudiantes,entregables, prueba, formulario,profesor_eliminar,profesor_actualizar,ProfesroListView,ProfesorCrear,ProfesorModificar, ProfesroEliminar, ProfesroDetail



urlpatterns = [
    path('crearcurso/<nombre>/<camada>', crear_curso),
    path("", inicio, name="inicio"),
    path("prueba", prueba, name='prueba'),
    path("cursos", cursos, name="cursos"),
    # path("profesores", profesores, name="profesores"),
    path("estudiantes", estudiantes, name="estudiantes"),
    path("entregables", entregables, name="entregables"),
    path("formulario", formulario, name="formulario"),
    # path("profe/eliminar/<id>",profesor_eliminar, name= 'profesor/eliminar' ),
    # path("profe/actualizar/<id>",profesor_actualizar, name= 'profesor/actualizar' ),
    path("profesores", ProfesroListView.as_view(), name="profesores"),
    path("profesor/añadir", login_required(ProfesorCrear.as_view()), name="profesores/añadir"),
    path("profe/actualizar/<pk>", login_required(ProfesorModificar.as_view()), name= 'profesor/actualizar' ),
    path("profe/eliminar/<pk>",login_required(ProfesroEliminar.as_view()), name= 'profesor/eliminar' ),
    path("profe/detalles/<pk>",ProfesroDetail.as_view(), name= 'profesor/detalles' ),
    path("agregar/avatar",agregar_avatar, name='agregar_avatar')
    
]