from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Articulo_form(forms.Form):
    titulo = forms.CharField(required=True)
    subtitulo = forms.CharField(required=True) 
    autor = forms.CharField()
    cuerpo = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    imagen = forms.ImageField()
