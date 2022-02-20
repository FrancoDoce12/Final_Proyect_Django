from dataclasses import fields
from datetime import datetime
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.contrib.auth.models import User


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView

from .forms import CursosForm,ProfesoresForm,AvatarForm,PostForm

from .models import Avatar, Curso, Profesor, Post


def helpp(request):
    return render(request, 'AppCoder/help.html')


def crear_curso(request, camada,nombre):
    camada_int = int(camada)
    curso = Curso(nombre = nombre, camada = camada_int)
    curso.save()
    
    return HttpResponse(f"Curso creadoo!!!  nombre: {curso.nombre} camada: {camada}")


def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    if request.method == "POST":
        formulario = ProfesoresForm(request.POST)
        
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data
            Profesor.objects.create(nombre= informacion['nombre'],
                                    apellido= informacion['apellido'],
                                    email= informacion['email'],
                                    profecion= informacion['profecion'])
        
        return redirect('profesores')
    
    else:
        formulario = CursosForm()
    
    
    return render(request,'AppCoder/profesores.html', {"profesores": Profesor.objects.all(),"formulario" : ProfesoresForm })
    
def estudiantes(request):
    return HttpResponse("vista de estudiantes")
    
def entregables(request):
    return HttpResponse("vista de entregables")

def inicio(request):
    if request.user.is_authenticated:
        
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            avatar_url =avatar.last().imagen.url
        else:
            avatar_url=''
    else:
        avatar_url=''
        
    
    ultimo_post = Post.objects.last()
    ultimo_usuario = User.objects.last()
    
    return render(request,'AppCoder/inicio.html',
                  {'avatar_url':avatar_url,'ultimo_post':ultimo_post,'ultimo_usuario':ultimo_usuario}
                  )

def formulario(request):
    if request.method == "POST":
        formulario = CursosForm(request.POST)
        
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data
            Curso.objects.create(nombre= informacion['curso'],camada= informacion['camada'])
        
        return redirect('prueba')
    
    else:
        formulario = CursosForm()
    
    return render(request, 'AppCoder/formulario.html',{'formulario' : formulario})

def profesor_eliminar(request, id):
    profe= Profesor.objects.get(id=id)
    profe.delete()
    
    return redirect('profesores')

def profesor_actualizar(request, id):
    profe= Profesor.objects.get(id=id)
    print(profe.id)
    
    if request.method == "POST":
        formulario = ProfesoresForm(request.POST)
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            profe.nombre = info['nombre']
            profe.apellido = info['apellido']
            profe.email = info['email']
            profe.profecion = info['profecion']
            
            profe.save()
            
            return redirect('profesores')
    
    else:
        formulario = ProfesoresForm(model_to_dict(profe))
    return render(request, 'AppCoder/formulario.html' ,{'formulario' : formulario})


# clase con login requierd

# class ProfesroListView(LoginRequiredMixin,ListView):
#    model = Profesor
#    template_name = 'AppCoder/profesores.html'
#    context_object_name= 'profesores' 
    
class ProfesroListView(ListView):
    model = Profesor
    template_name = 'AppCoder/profesores.html'
    context_object_name= 'profesores'
    
class ProfesroDetail(DetailView):
    model = Profesor
    template_name = 'AppCoder/ver_profesores.html'

class ProfesorCrear(CreateView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre','apellido','email','profecion']
    template_name= 'AppCoder/formulario.html'
    
class ProfesorModificar(UpdateView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre','apellido','email','profecion']
    template_name= 'AppCoder/formulario.html'
    
class ProfesroEliminar(DeleteView):
    model = Profesor
    template_name = 'AppCoder/eliminar_profesores.html'
    success_url = reverse_lazy('profesores')

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            Avatar(user=request.user, imagen =formulario.cleaned_data['imagen'] ).save()
            
            return redirect('prueba')
        
    else:
        formulario= AvatarForm()
        
    return render(request, 'AppCoder/crear_avatar.html',{'form': formulario})



def bienvenido(request):
    return render(request, 'AppCoder/bienvenida.html')

@login_required
def crear_post(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            
            Post    (
                logo=formulario.cleaned_data['logo'],
                user=request.user,
                autor=request.user.username,
                fecha_de_creacion = datetime.now(),
                titulo =formulario.cleaned_data['titulo'],
                text =formulario.cleaned_data['text'],
                descripcion =formulario.cleaned_data['descripcion']
                     ).save()
            
            return redirect('inicio')
        
    else:
        formulario= PostForm()
        
    return render(request, 'AppCoder/crear_avatar.html',{'form': formulario})


class PostListView(ListView):
    model = Post
    template_name = 'AppCoder/ver_post.html'
    context_object_name= 'posts'
    
class PostDetail(DetailView):
    model = Post
    template_name = 'AppCoder/ver_post_detalle.html'


@login_required
def para_ti(request):
    return render(request, 'AppCoder/para_ti.html')


def busqueda_post(request):
    return render(request, 'AppCoder/post_buscar.html')


def buscar(request):
    
    if request.GET['titulo']:
        
        titulo = request.GET['titulo']
        
        posts = Post.objects.filter(titulo__icontains = titulo)
        
        return render(request, 'AppCoder/buscar.html',{'posts':posts, 'titulo':titulo})
    
    else:
        return HttpResponse("Busqueda invalida")