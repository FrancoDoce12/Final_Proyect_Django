from multiprocessing import context
from django.urls import path
from  django.contrib.auth.decorators import login_required

from AppCoder.views import crear_curso, bienvenido, buscar, busqueda_post, crear_post, para_ti ,PostDetail , PostListView, inicio, helpp, cursos, agregar_avatar,estudiantes,entregables, formulario,ProfesroListView,ProfesorCrear,ProfesorModificar, ProfesroEliminar, ProfesroDetail



urlpatterns = [
    path('crearcurso/<nombre>/<camada>', crear_curso),
    path("help",helpp,name='help'),
    path("inicio", inicio, name='inicio'),
    path("bienvenido", bienvenido, name='bienvenido'),
    path("para_ti", para_ti, name='para_ti'),
    path("crear_post", crear_post, name='crear_post'),
    path("post/view", PostListView.as_view(), name='post_view'),
    path("post/detail/<pk>", PostDetail.as_view(), name='post_detail'),
    path("post/buscar", busqueda_post, name='post_buscar'),
    path("buscar", buscar, name='buscar'),
    
    
    
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