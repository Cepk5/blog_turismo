from django.urls import path, include
from messageApp import views
from .views import *

urlpatterns = [
    path('messages/', Mensaje.as_view(), name ="message_list"),
    path('mensaje_form/', Mensaje_nuevo.as_view(), name="messages_new"),
]