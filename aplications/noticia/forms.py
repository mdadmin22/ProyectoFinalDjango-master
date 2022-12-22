from django import forms
from .models import Noticia




class FormularioNoticias( forms.ModelForm ):
    class Meta:
        model = Noticia
        fields = ('__all__')



