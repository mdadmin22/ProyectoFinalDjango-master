from time import timezone
from django.db import models

# Create your models here.
#from aplications.usuario.models import Usuario
from aplications.noticia.models import Noticia

# Create your models here.

class Comentarios(models.Model):

    fecha_hora_registro = models.DateTimeField(auto_now_add=True)
    comentarios = models.CharField('Comentario', max_length=2000, blank=True)
    noticia = models.ForeignKey(Noticia, related_name= 'noticias', on_delete=models.SET_NULL, null=True )

    me_gusta = models.BooleanField(default=False)

    def __str__(self) :
        return  str(self.comentarios)