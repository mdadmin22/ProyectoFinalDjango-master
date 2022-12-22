from django.urls import path
from .import views



urlpatterns = [
    path('comentario/', views.ComentarioCreateView.as_view(), name='comentario')
]       