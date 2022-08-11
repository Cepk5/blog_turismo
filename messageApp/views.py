from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from messageApp.models import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

class Mensaje(ListView, LoginRequiredMixin):
    model = Message
    template_name = "messageApp/messages.html"

class Mensaje_nuevo(CreateView, LoginRequiredMixin):
    model = Message
    template_name = "messageApp/mensaje_form.html"
    success_url = reverse_lazy('message_list')
    fields = ['recibe', 'mensaje']

    def form_valid(self, form):
        form.instance.envia = self.request.user
        return super().form_valid(form)
