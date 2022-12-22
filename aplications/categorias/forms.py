from django import forms
from .models import Categorias


class FormularioCategorias( forms.ModelForm ):
    class Meta:
        model = Categorias
        fields = ('__all__')


