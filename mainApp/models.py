from django.db import models
import datetime

# Create your models here.

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=70)
    #region deberia venir de otra tabla como foreignKey
    region = models.CharField(max_length=40)
    #usuario deberia ser una ForeingnKey que trae de BD de usuarios?? 
    autor = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #vemos como hacemos la fecha de mod sino la sacamos
    fecha_mod = models.DateTimeField(auto_now=True)
    #chequear que este bien lo de la imagen:
    #imagen = models.ImageField(upload_to = 'media', null = True, blank = True)
    
    #fecha_string = fecha_mod.ToString("dd/MM/yyy")
    def __str__(request):
        return f'{request.titulo}, {request.region}, {request.autor}, Fecha modificación: {request.fecha_mod.strftime("%d/%m/%Y-%H:%M:%S")}'
