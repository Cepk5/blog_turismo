from django.urls import path, include
from mainApp import views
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name ='Login'),
    #path('', include('mainApp.urls')),
    path('signup/', views.register, name ='Register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name ='Logout'),
    path('profile/', views.editarPerfil, name='Editar_perfil'),
    path('agregarAvatar/<pk>', views.agregarAvatar, name='agregarAvatar'),
    #al mensaje lo hago desde aca o desde la app messageApp?
    #path('messageApp/messages', views.mensaje, name="mensaje"),
]
