from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import *

class Homepage(TemplateView):
    template_name = 'entrada/index.html'

class Desenvolvedores(TemplateView):
    template_name = 'entrada/desenvolvedores.html'


class Sobre(TemplateView):
    template_name = 'entrada/sobre.html' 


class Contato(TemplateView):
    template_name = 'entrada/contato.html'


class DetalhesEstacaoView(DetailView):
    model = Estacoe
    template_name = 'estacoes/detalhes_estacao.html'
    context_object_name = 'estacao'
    
    def get_object(self):
        nome_estacao = self.kwargs.get('nome')
        return Estacoe.objects.get(nome=nome_estacao)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega a estação atual
        estacao_atual = self.get_object()        
        # Carregar instâncias de cada modelo
        context['estacoes'] = Estacoe.objects.all()
        context['paleta_cor_list'] = Paleta_Core.objects.filter(nome=estacao_atual.cor)
        context['img_equipes'] = Imagens_equipe.objects.filter(estacao=estacao_atual)
        context['img_beneficios_cores'] = Imagens_Beneficios_Core.objects.filter(cor=estacao_atual.cor)[:3]
        context['img_ideais_para'] = Imagens_Ideal_Para_Core.objects.filter(cor=estacao_atual.cor)[:3]
        
        context['range_simulado'] = range(1, 4)
        
        return context

    

class Teste2View(TemplateView):
    template_name = 'entrada/teste2.html'
    
    def get_object(self):
        nome_estacao = self.kwargs.get('nome')
        return Estacoe.objects.get(nome=nome_estacao)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega a estação atual
        estacao_atual = self.get_object()        
        # Carregar instâncias de cada modelo
        context['estacoes'] = Estacoe.objects.all()
        context['img_equipes'] = Imagens_equipe.objects.all()
        context['img_beneficios_cores'] = Imagens_Beneficios_Core.objects.filter(cor=estacao_atual.cor)[:3]
        context['img_ideais_para'] = Imagens_Ideal_Para_Core.objects.all()
        
        return context