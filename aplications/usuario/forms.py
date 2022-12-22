from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm



class FormularioUsuario( UserCreationForm ):
    class Meta:
        model = Usuario
        fields = ("first_name", "last_name", "email", "username", "password1", "password2","celular","fecha_de_nacimiento",)
        