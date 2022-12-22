from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView

# Create your views here.

from django.views.generic import ListView, DetailView

from .models import Noticia
from .forms import FormularioNoticias



#conect = DATABASES.

class ListarNoticias(ListView):
    
    template_name = 'noticia/noticias_varias.html'
    model = Noticia




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.all()
        return context






class PaginaInicio(TemplateView):
    template_name = "base.html"



class NoticiasCreateView(CreateView):
    template_name = 'noticia/noticia.html'
    model = Noticia
    form_class = FormularioNoticias


    def get_success_url(self):
        return reverse_lazy('vernoticias')


    def form_valid(self, form):
        return super(NoticiasCreateView, self).form_valid(form)


class MostrarNoticias(ListView):
    
    template_name = 'noticia/mostrarnoticia.html'
    model = Noticia


    def get_context_data(self, **kwargs):
        print ("################")
               
        context = super().get_context_data(**kwargs)      
        context["noticias"] = Noticia.objects.all()
        return context
    
    
class MostrarDetalleNoticia(DetailView):
    # specify the model to use
    model = Noticia
    template_name = 'noticia/mostrarnoticia.html'
 
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)      
        # comentarios = Comentarios.objects.filter(noticia_id=context["noticia"].id)
        # context["comentarios"] = comentarios  ---->> hacer for
        return context

