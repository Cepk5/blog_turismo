from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Message(models.Model):
    envia = models.ForeignKey(User, related_name="envia", on_delete = models.CASCADE)
    recibe = models.ForeignKey(User, related_name="recibe", on_delete = models.CASCADE)
    mensaje = RichTextField(blank=True,null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(request):
        return f'Mensaje de: {request.envia},. Para: {request.recibe}. {request.fecha.strftime("%d/%m/%Y-%H:%M")}'