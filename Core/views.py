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

class EscolherEstacao(TemplateView):
    template_name = 'estacoes/escolher_estacao.html'

class EstacaoDetail(DetailView):
    model = Estacao
    template_name = 'estacoes/estacao_detail.html'

