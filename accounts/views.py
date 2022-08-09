from urllib import request
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from accounts.forms import UserRegisterForm, UserEditForm, UserCreationForm, AvatarForm
from django.contrib.auth.decorators import login_required


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
            
@login_required
def editarPerfil(request):

    usuario=request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion ['email']
            usuario.password1 = informacion ['password1']
            usuario.password2 = informacion ['password2']
            usuario.last_name = informacion ['last_name']
            usuario.first_name = informacion ['first_name']
            usuario.save()

            return render(request, 'mainApp/index.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, 'accounts/profile.html', {"miFormulario": miFormulario, "usuario": usuario.username})

@login_required
def agregarAvatar(request):
    if request == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            AvatarViejo = Avatar.objects.get(user=request.user)
            if (AvatarViejo.avatar):
                AvatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data ['imagen'])
            avatar.save()
    else:
        formulario = AvatarForm()
    return render(request, 'accounts/agregarAvatar.html', {'formulario': formulario, 'usuario':request.user})
