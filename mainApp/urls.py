from django.urls import path
from mainApp import views
from .views import *


urlpatterns = [
    path('', views.index),
    path('index/', views.index, name="Index"),
    path('about', views.about, name="About"),
    #path('pages', views.listar_art, name="paginas"),
    #path('crear_articulo', views.crear_art, name="crear_articulo"),
    #path('borrar_articulo/<pagina>/', views.eliminar_art, name="eliminar_articulo"),
    path('pages', Articulo_list.as_view(), name='List'),
    path('pages/<pk>', Articulo_det.as_view(), name='Detail'),
    path('articulo_form', Articulo_new.as_view(), name="Create"),
    path('editar/<pk>', Articulo_update.as_view(), name="Edit"),
    path('articulo_confirm_delete/<pk>', Articulo_del.as_view(), name="Delete"),
    #path('pages', views.listar_art, name="paginas"),
    #path('agregarAvatar/<pk>', views.agregarAvatar, name='agregarAvatar'),
    #al mensaje lo hago desde aca o desde la app messageApp?
    #path('messageApp/messages', views.mensaje, name="mensaje"),
]
"""
completar las views."FUNCION" como corresponda
path('about', views., name=""),
path('articulos', views., name=""),
path('borrar_articulo', views., name=""),
path('crear_articulo', views., name=""),
"""