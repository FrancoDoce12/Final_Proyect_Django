from django.urls import path


from AppCoder.views import crear_curso, inicio, cursos, profesores,estudiantes,entregables, prueba, formulario,profesor_eliminar,profesor_actualizar

urlpatterns = [
    path('crearcurso/<nombre>/<camada>', crear_curso),
    path("", inicio, name="inicio"),
    path("prueba", prueba, name="prueba"),
    path("cursos", cursos, name="cursos"),
    path("profesores", profesores, name="profesores"),
    path("estudiantes", estudiantes, name="estudiantes"),
    path("entregables", entregables, name="entregables"),
    path("formulario", formulario, name="formulario"),
    path("profe/eliminar/<id>",profesor_eliminar, name= 'profesor/eliminar' ),
    path("profe/actualizar/<id>",profesor_actualizar, name= 'profesor/actualizar' ),
    
]