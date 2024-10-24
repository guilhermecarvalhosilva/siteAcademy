from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Estacao

# Create your views here.
class Homepage(TemplateView):
    template_name = 'entrada/index.html'

class Sobre(TemplateView):
    template_name = 'entrada/sobre.html' 

class Contato(TemplateView):
    template_name = 'entrada/contato.html'


class DetalhesEstacaoView(DetailView):
    model = Estacao
    template_name = 'estacoes/detalhes_estacao.html'
    context_object_name = 'estacao'
    