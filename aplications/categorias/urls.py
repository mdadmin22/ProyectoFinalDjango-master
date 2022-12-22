from django.contrib import admin
from django.urls import path, include

from . import views  

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('usuario/', views.CargarNoticia.as_view()),
    
    #path('login/', views.Login.as_view()),
    #path('noticia/', views.ListarNoticias.as_view(), name='vernoticias'),
    path('nueva-categoria/', views.CategoriasCreateView.as_view(), name='nuevacategoria'),
    

    
]       