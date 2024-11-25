from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

class Homepage(ListView):
    template_name = 'entrada/index.html'
    model = Estacoe
    context_object_name = "estacoes"

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
    




@login_required
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            # Adicionar o usuário ao grupo selecionado
            group = form.cleaned_data.get('groups')
            if group:
                group.user_set.add(user)
            
            messages.success(request, f'Usuário {user.username} foi criado com sucesso!')
            return redirect('some_view_name')  # Redirecione para uma página apropriada
    else:
        form = CustomUserCreationForm()

    return render(request, 'entrada/add_user.html', {'form': form})
