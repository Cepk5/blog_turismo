from django.urls import path, include
from mainApp import views
from accounts import views

urlpatterns = [
    path('messages/', views.login_request, name ='Message'),
    #path('',include('mainApp.urls')),
    #al mensaje lo hago desde aca o desde la app messageApp?
    #path('messageApp/messages', views.mensaje, name="mensaje"),
]
