from django.db import models


#from applications.usuario.models import Usuarios

from aplications.usuario.models import Usuario
from aplications.categorias.models import Categorias

# Create your models here.

class Noticia(models.Model):

    categorias = models.ForeignKey(Categorias,related_name= 'categorias', on_delete=models.SET_NULL, null=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField('Titulo', max_length=50)
    fecha_noticia = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='noticia', null=True, blank=True)
    subtitulo_detalles = models.CharField('Subtitulo', max_length=100)
    texto = models.TextField('Texto', max_length=2000)
    
    def __str__(self):
        x= self.titulo
        return x