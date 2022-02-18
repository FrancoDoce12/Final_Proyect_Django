from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, IntegerField, EmailField, DateField, BooleanField, TextField
from django.contrib.auth.models import User

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
    
    def __str__(self):
        return  f"Profesor: {self.nombre} {self.apellido} Email: {self.email}, Profe de {self.profecion}"
    
    
class Entregable(Model):
    nombre = CharField(max_length = 30)
    fecha_de_entrega = DateField()
    entregado = BooleanField()
    
class Post(Model):
    descripcion = TextField()
    text = TextField()
    titulo = CharField(max_length = 30)
    autor= CharField(max_length=20)
    fecha_de_creacion = DateField()
    user = ForeignKey(User, on_delete=CASCADE)
    logo = ImageField(upload_to = 'posts', null=True,blank=True)
    


class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to = 'avatares', null=True,blank=True)