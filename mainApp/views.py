from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import *
from mainApp.forms import Articulo_form
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class Articulo_new(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = reverse_lazy('List')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'region']

class Articulo_update(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = reverse_lazy('List')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'region']

class Articulo_del(LoginRequiredMixin, DeleteView):
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

