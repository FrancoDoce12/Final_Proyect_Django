from django.shortcuts import render
from django.http import HttpResponse
from django.db.backends import mysql

from .models import Curso

def crear_curso(request, camada,nombre):
    camada_int = int(camada)
    curso = Curso(nombre = nombre, camada = camada_int)
    curso.save()
    
    return HttpResponse(f"Curso creadoo!!!  nombre: {curso.nombre} camada: {camada}")

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return HttpResponse("vista de cursos")

def profesores(request):
    return HttpResponse("vista de profesores")
    
def estudiantes(request):
    return HttpResponse("vista de estudiantes")
    
def entregables(request):
    return HttpResponse("vista de entregables")
