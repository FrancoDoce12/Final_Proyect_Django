from django.urls import path


from AppCoder.views import crear_curso, inicio, cursos, profesores,estudiantes,entregables

urlpatterns = [
    path('crearcurso/<nombre>/<camada>', crear_curso),
    path("", inicio),
    path("cursos", cursos),
    path("profesores", profesores),
    path("estudiantes", estudiantes),
    path("entregables", entregables),
]