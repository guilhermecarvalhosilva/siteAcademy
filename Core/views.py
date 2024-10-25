from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Estacao, Paleta_Core, Servico, Beneficio, Imagens_equipe

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Acessa a Paleta_Core associada à Estacao
        context['paleta_cor'] = self.object.cor
        
        # Obtém serviços relacionados à paleta de cor
        context['servicos'] = Servico.objects.filter(cor=self.object.cor)[0:3]
        
        # Obtém benefícios relacionados à paleta de cor
        context['beneficios'] = Beneficio.objects.filter(cor=self.object.cor)[0:3]
        
        # Obtém imagens da equipe da estação
        context['imagens_equipe'] = Imagens_equipe.objects.filter(estacao=self.object)

        
        return context
