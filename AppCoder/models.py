from django.db.models import Model
from django.forms import CharField, IntegerField, EmailField, DateField ,BooleanField

class Curso(Model):
    nombre = CharField(max_length = 40)
    camada = IntegerField()


class Estudiante(Model):
    nombre = CharField(max_length = 30)
    apellido = CharField(max_length = 30)
    email = EmailField()

class Profesor(Model):
    nombre = CharField(max_length = 30)
    apellido = CharField(max_length = 30)
    email = EmailField()
    
    profecion = CharField(max_length = 30)
    
class Entregable(Model):
    nombre = CharField(max_length = 30)
    fecha_de_entrega = DateField()
    entregado = BooleanField()
