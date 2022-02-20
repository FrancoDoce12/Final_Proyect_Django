from  dataclasses import fields
from  django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from  django.contrib.auth import login,logout,authenticate
from  django.contrib.auth.decorators import login_required
from  django.http import HttpResponse
from  django.shortcuts import render,redirect
from  Proyecto_Final_Coder.forms import UserRegistrationForm,UserEditForm
from  django.views.generic import CreateView,DetailView,ListView
from  django.contrib.auth.models import User
from  django.urls import reverse_lazy

def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(username=usuario, password = contraseña)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            
            else:
                return render(request, 'login.html', {'form': form, 'error': 'No es valio el Usuario'})
            
        else:
            return render(request, 'login.html', {'form': form})
        
    else :
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    
def login_request_default(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(username=usuario, password = contraseña)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            
            else:
                return render(request, 'login_default.html', {'form': form, 'error': 'No es valio el Usuario'})
            
        else:
            return render(request, 'login_default.html', {'form': form})
        
    else :
        form = AuthenticationForm()
        return render(request, 'login_default.html', {'form': form})
    
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'loginsuccsesful.html',{'username':username})
        else:
            return render(request, 'loginfail.html')
            
    else:
        form = UserRegistrationForm()
        return render(request, 'AppCoder/inicio.html',{'form': form })
    
class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('Coder/inicio')
    template_name = 'registro.html'
    form_class = UserRegistrationForm
    
class UserDetailView(DetailView):
    model = User
    template_name = 'miPerfil.html'
    
    
@login_required
def editar_perfil(request):
    user = request.user
    
    if request.method == 'POST':
        
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user.email = data['email']
            user.set_password(data['password1'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            return redirect('prueba')
        
    else:
        formulario = UserEditForm({'email': user.email})
        
    return render(request,'editar_perfil.html', {'form':formulario})


class UserListView(ListView):
    model = User
    template_name = 'social.html'
    context_object_name= 'users'
    
    
def myself(request):
    return render(request, 'sobre_mi.html')





    