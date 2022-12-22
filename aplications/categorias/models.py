from django.db import models
#from aplications.noticia.models import Noticia

# Create your models here.

class Categorias(models.Model):
    nombre_categoria = models.CharField( max_length=50,null=False, unique=True)

   
    def __str__(self) :
        return  (self.nombre_categoria)