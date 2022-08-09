from django.shortcuts import render
from django.http import HttpResponse
import mainApp
from mainApp.models import *
from mainApp.forms import Articulo_form
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from mainApp.forms import Articulo_form, UserEditForm, UserCreationForm, UserRegisterForm, AvatarForm
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib import messages


#Superuser 
"""
class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(request):
        return self.request.user.is_superuser
"""
class SuperUserRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, "mainApp/sin_autorizacion.html")
        return super(SuperUserRequiredMixin, self).dispatch(request,*args, **kwargs)

# Create your views here.

def index(request):
    return render(request, "mainApp/index.html")

def about(request):
    return render(request, "mainApp/about.html")

def pages(request):
    return render(request, "mainApp/pages.html")

#crear articulo en el blog (Crud)
"""
def crear_art(request):

    if request.method == 'POST': #VER COMO AGREGAR AUTOR QUE SE SACARIA DEL QUE ESTA LOGUEADO, FECHA CON GETDATE? y recibir imagen

        formulario = Articulo_form(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            articulo = Articulo(titulo=info['titulo'], subtitulo=info['subtitulo'], autor=info['autor'], cuerpo=info['cuerpo'],fecha_creacion=info['fecha_creacion'], fecha_mod=info['fecha_mod'], imagen=info['imagen'])
            
            articulo.save()

            #VER DE QUE MANDE O MUESTRE UN MENSAJE QUE LA PUBLICACION SE CREO CON EXITO
            return render(request, "mainApp/index.html")
    else:

        formulario = Articulo_form()

    return render(request, "mainApp/crear_articulo.html", {"formulario":formulario})

#listar articulos del blog (cRud)
def listar_art(request):

    articulos = Articulo.objects.all()

    contexto = {"articulos":articulos}

    return render(request, "mainApp/pages.html", contexto)
"""
#Clases basadas en vistas
class Articulo_list(ListView):
    model = Articulo
    template_name = "mainApp/pages.html"

class Articulo_det(DetailView):
    model = Articulo
    template_name = "mainApp/pages_detalle.html"
    
class Articulo_new(LoginRequiredMixin, SuperUserRequiredMixin, CreateView):
    model = Articulo
    success_url = reverse_lazy('List')
    fields = ['titulo', 'subtitulo', 'autor', 'cuerpo', 'region', 'imagen']

class Articulo_update(LoginRequiredMixin, SuperUserRequiredMixin, UpdateView):
    model = Articulo
    success_url = reverse_lazy('List')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'region', 'imagen']

class Articulo_del(LoginRequiredMixin, SuperUserRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('List')

#eliminar articulo del blog (cruD)
"""
def eliminar_art(request, pagina):

    articulo = Articulo.objects.get(titulo=pagina)
    articulo.delete()

    articulos = Articulo.objects.all()

    contexto = {"articulos":articulos}

    return render(request, "mainApp/pages.html", contexto)
"""
"""
AGREGO JUANJO, lo pase a accounts/views
def agregarAvatar(request):
    if request == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            AvatarViejo = Avatar.objects.get(user=request.user)
            if (AvatarViejo.avatar):
                AvatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data ['imagen'])
            avatar.save
    else:
        formulario = AvatarForm()
    return render(request, 'mainApp/agregarAvatar.html', {'formulario': formulario, 'usuario':request.user})
"""

