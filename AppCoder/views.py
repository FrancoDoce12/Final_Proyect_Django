from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

def crear_curso(request, camada):
    curso = Curso(nombre = 'CACA', camada = camada)
    curso.save()
    
    HttpResponse(f"Curso creadoo!!! {camada}")
    