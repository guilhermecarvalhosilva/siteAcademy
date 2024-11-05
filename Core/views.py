from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Estacao, Paleta_Core, Servico, Beneficio, Imagens_equipe, Imagens_beneficios_core, Ideal_para

class Homepage(TemplateView):
    template_name = 'entrada/index.html'

class Desenvolvedores(TemplateView):
    template_name = 'entrada/desenvolvedores.html'


class Sobre(TemplateView):
    template_name = 'entrada/sobre.html' 


class Contato(TemplateView):
    template_name = 'entrada/contato.html'


class DetalhesEstacaoView(DetailView):
    model = Estacao
    template_name = 'estacoes/detalhes_estacao.html'
    context_object_name = 'estacao'
    
    def get_object(self):
        nome_estacao = self.kwargs.get('nome')
        return Estacao.objects.get(nome=nome_estacao)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega a estação atual
        estacao_atual = self.get_object()
        
        # Filtra os serviços que têm a mesma cor da estação
        context['servicos'] = Servico.objects.filter(cor=estacao_atual.cor)[:3]
        context['beneficios'] = Beneficio.objects.filter(cor=estacao_atual.cor)[:3]
        
        return context

    

class TesteView(TemplateView):
    template_name = 'entrada/teste.html'
    
    def get_object(self):
        nome_estacao = self.kwargs.get('nome')
        return Estacao.objects.get(nome=nome_estacao)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega a estação atual
        estacao_atual = self.get_object()        
        # Carregar instâncias de cada modelo
        context['estacoes'] = Estacao.objects.all()
        context['servicos'] = Servico.objects.filter(cor=estacao_atual.cor)[:3]
        context['beneficios'] = Beneficio.objects.filter(cor=estacao_atual.cor)[:3]
        context['imagens_equipes'] = Imagens_equipe.objects.all()
        context['imagens_beneficios_cores'] = Beneficio.objects.filter(cor=estacao_atual.cor)[:3]
        context['ideais_para'] = Ideal_para.objects.all()
        
        return context