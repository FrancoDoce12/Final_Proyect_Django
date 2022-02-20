"""Proyecto_Final_Coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from Proyecto_Final_Coder.views import login_request,login_request_default, myself,editar_perfil,UserCreateView,UserDetailView,UserListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Coder/", include('AppCoder.urls')),
    path("login",login_request, name= 'login'),
    path("login_default",login_request_default, name= 'login_default'),
    path("registro",UserCreateView.as_view(), name= 'registro'),
    path("user/profile/<pk>",UserDetailView.as_view(), name= 'user_profile'),
    path("logout",LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('useredit',login_required(editar_perfil), name='user_edit'),
    path('social',login_required(UserListView.as_view()), name='social'),
    path('sobremi',myself, name='sobremi'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
