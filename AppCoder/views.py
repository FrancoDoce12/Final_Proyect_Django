from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.backends import mysql

from .forms import CursoForm,ProfesoresForm

from .models import Curso, Profesor

def crear_curso(request, camada,nombre):
    camada_int = int(camada)
    curso = Curso(nombre = nombre, camada = camada_int)
    curso.save()
    
    return HttpResponse(f"Curso creadoo!!!  nombre: {curso.nombre} camada: {camada}")

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

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
        formulario = CursoForm()
    
    
    return render(request,'AppCoder/profesores.html', {"profesores": Profesor.objects.all(),"formulario" : ProfesoresForm })
    
def estudiantes(request):
    return HttpResponse("vista de estudiantes")
    
def entregables(request):
    return HttpResponse("vista de entregables")

def prueba(request):
    return render(request,'AppCoder/inicio_prueba.html')

def formulario(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data
            Curso.objects.create(nombre= informacion['curso'],camada= informacion['camada'])
        
        return redirect('prueba')
    
    else:
        formulario = CursoForm()
    
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
        #print(formulario.cleaned_data())
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            profe.nombre = info['nombre']
            profe.apellido = info['apellido']
            profe.email = info['email']
            profe.profecion = info['profecion']
            
            return redirect('profesores')
    
    else:
        formulario = ProfesoresForm(model_to_dict(profe))
    return render(request, 'AppCoder/formulario.html' ,{'formulario' : formulario})