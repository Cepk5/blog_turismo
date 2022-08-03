from urllib import request
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from accounts.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            usuario = authenticate(username=usuario, password=clave)

            if usuario is not None:
                login(request, usuario)
        
                return render(request, "mainApp/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "mainApp/index.html", {"mensaje": "Usuario o clave incorrecta"})

        else:
            return render(request, "accounts/login.html", {"mensaje": "FORMULARIO INVALIDO"})

    else:
        form = AuthenticationForm()
        return render (request, "accounts/login.html", {'form': form})


def register(request):

    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "mainApp/index.html", {"mensaje": "Usuario Creado"})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "accounts/signup.html", {"form":form})
            