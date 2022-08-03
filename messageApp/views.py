from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mensajes(request):
    return render(request, "messageApp/messages.html")