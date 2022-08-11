from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Articulo(models.Model):
    #ID se autogenera
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=70)
    #region deberia venir de otra tabla como foreignKey, pero puede quedar asi por ahora
    region = models.CharField(max_length=40)
    #Se elige de Users 
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    cuerpo = RichTextField(blank=True,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #Fecha de modificacion del articulo
    fecha_mod = models.DateTimeField(auto_now=True)
    #Imagen se guarda en "Posts" y carpeta con fecha de subida
    imagen = models.ImageField(upload_to = 'Posts/%d/%m/%Y', null = True, blank = True)
    
    #Como muestro el objeto
    def __str__(request):
        return f'{request.id},{request.titulo},{request.autor}, {request.fecha_mod.strftime("%Y/%m/%d-%H:%M:%S")}'
