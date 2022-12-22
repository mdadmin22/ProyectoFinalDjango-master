from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Comentarios
from .forms import FormularioComentarios
# Create your views here.



class ComentarioCreateView(CreateView):
    model = Comentarios
    template_name = "comentario/comentario.html"
    form_class = FormularioComentarios
    success_url= reverse_lazy('comentario')


    def form_valid(self, form):
        return super().form_valid(form)

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentarios.objects.all()
        return context