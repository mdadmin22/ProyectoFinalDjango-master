from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):

    phone_message = 'Phone number must be entered in the format: 05999999999'
    phone_regex = RegexValidator( regex=r'\d{9}$', message=phone_message )
    
    tipo = models.BooleanField(default=False)
    
    celular =  models.CharField( validators=[phone_regex], max_length=60,null=True, blank=True )
    fecha_de_nacimiento = models.DateField(null=True)
        

    def __str__(self):
        return   self.get_full_name()


