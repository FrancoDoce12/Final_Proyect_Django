from django.forms import Form, CharField, IntegerField,BooleanField,EmailField,ImageField,DateField


class CursosForm(Form):
    
    nombre = CharField(max_length=20)
    camada = IntegerField(max_value=999999)
    sos_gay = BooleanField()
    
class ProfesoresForm(Form):
    
    nombre = CharField(max_length=20)
    apellido = CharField(max_length=20)
    email = EmailField(max_length=20)
    profecion = CharField(max_length=20)
    
class AvatarForm(Form):
    imagen = ImageField(required=True)
    
class PostForm(Form):
    descripcion = CharField(max_length = 60)
    text = CharField(max_length = 1000)
    titulo = CharField(max_length = 25)
    logo = ImageField(required=False)
    