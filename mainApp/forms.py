from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Articulo_form(forms.Form):
    titulo = forms.CharField(required=True)
    subtitulo = forms.CharField(required=True) 
    autor = forms.CharField()
    cuerpo = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    imagen = forms.ImageField()
"""
AGREGO JUANJO, lo pase a accounts/url
class UserEditForm(forms.Form):
    email = forms.EmailField(label='modificar E-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

class Meta: 
    model = User
    fields = ['email', 'password1', 'password2']
    help_texts = {k:'' for k in fields}

class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='modificar E-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField
    first_name = forms.CharField

class Meta: 
    model = User
    fields = ['email', 'password1', 'password2']
    help_texts = {k:'' for k in fields}

class UserCreationForm(forms.Form):
    email = forms.EmailField(label= 'E-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField
    first_name = forms.CharField

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label = 'Imagen')
"""


    #fecha_creacion = forms.DateTimeField()
    #vemos como hacemos la fecha de mod sino la sacamos
    #fecha_mod = forms.DateTimeField()
    #chequear que este bien lo de la imagen:
    #imagen = forms.ImageField(upload_to = 'media', null = True, blank = True)
