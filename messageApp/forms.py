from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#Formulario para crear mensaje nuevo
class Mensaje_form(forms.Form):
    recibe = forms.CharField(required=True)
    envia = forms.CharField()
    mensaje = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'ckeditor'}))

