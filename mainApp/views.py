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
from django.utils.decorators import method_decorator
from django.contrib import messages


#Superuser 
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

#CRUD Clases basadas en vistas
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


