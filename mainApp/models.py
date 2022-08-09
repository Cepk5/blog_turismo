from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=70)
    #region deberia venir de otra tabla como foreignKey, pero puede quedar asi por ahora
    region = models.CharField(max_length=40)
    #usuario deberia ser una ForeingnKey que trae de BD de usuarios?? 
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    cuerpo = RichTextField(blank=True,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #vemos como hacemos la fecha de mod sino la sacamos
    fecha_mod = models.DateTimeField(auto_now=True)
    #chequear que este bien lo de la imagen:
    imagen = models.ImageField(upload_to = 'Posts', null = True, blank = True)
    
    #fecha_string = fecha_mod.ToString("dd/MM/yyy")
    def __str__(request):
        return f'({request.id},{request.titulo},{request.autor}, {request.fecha_mod.strftime("%Y/%m/%d-%H:%M:%S")})'

""" Agrego juanjo lo llevo a accouns/models
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
"""