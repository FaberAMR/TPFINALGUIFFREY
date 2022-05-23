from click import password_option
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View, CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#from django.core.urlresolvers import reverse_lasy



# Create your views here.
'''class registroUsuario(CreateView):
    model = User
    template_name = "appUsuarios/registro.html"
    form_class = UserCreationForm
    success_url = reverse_lasy ('blog:blogList')
'''
def usuarios(request):
    return render(request, "usuarios/registro.html")

class registroUsuario(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "usuarios/registro.html", {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario1=form.save()
            login(request, usuario1)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "usuarios/registro.html", {"form":form})


def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def loguear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "informacion incorrecta")
    form=AuthenticationForm()
    return render(request, "login/login.html", {"form":form})
