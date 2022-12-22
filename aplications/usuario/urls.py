from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Salir


from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('registro/', views.UsuarioCreateView.as_view(), name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name="usuario/login.html"), name='login'),
    path('exito/', views.Exito.as_view(), name='exito'),
    path('salir/', Salir, name='salir')
]       