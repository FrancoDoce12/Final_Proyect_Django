from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField,CharField,PasswordInput

class UserRegistrationForm(UserCreationForm):
    
    email = EmailField()
    password1 =CharField(label='Contraseña',widget=PasswordInput)
    password2 =CharField(label='Confirmar contraseña',widget=PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = EmailField(label='modifica tu Email')
    password1 =CharField(label='Contraseña',widget=PasswordInput)
    password2 =CharField(label='Confirmar contraseña',widget=PasswordInput)
    first_name = CharField(label='Nombre',max_length=20,required=False)
    last_name = CharField(label='Apellido',max_length=20,required=False)
    
    class Meta:
        model = User
        fields = ['email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}
        
