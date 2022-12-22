from django import forms
from .models import Comentarios


class FormularioComentarios( forms.ModelForm ):
    class Meta:
        model = Comentarios
        fields = ('comentarios', 'me_gusta', 'noticia')
        widgets = {
            'comentarios': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese su comentario',
                    'cols': "80",
                    'rows':"5",
                    'margin': "0"
                }
            )
        }


