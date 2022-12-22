from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Categorias
from .forms import FormularioCategorias
from django.urls import reverse_lazy

# Create your views here.

class CategoriasCreateView(CreateView):
    template_name = 'categorias/categorias.html'
    model = Categorias
    form_class = FormularioCategorias
    success_url= reverse_lazy('noticias')

    def form_valid(self, form):
        return super().form_valid(form)