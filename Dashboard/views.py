from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Projeto

class IndexDashboardView(ListView):
    template_name = "index_dashboard.html"
    model = Projeto
    context_object_name = "projetos"


class BaseView(ListView):
    template_name = "bases/menu_lateral.html"
    model = Projeto
    context_object_name = "projetos"


class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = "projeto_detail.html"
    context_object_name = "projeto"

class ListEstacaoView(ListView):
    template_name = "list_dashboard.html"
    model = Projeto
    context_object_name = "projetos_get"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['total_em_andamento'] = queryset.filter(status="Em_andamento").count()
        context['stand_by'] = queryset.filter(status="Standy-by").count()
        context['concluido'] = queryset.filter(fase="Concluido").count()
        context['atrasado'] = queryset.filter(status="Atrasado").count()
        return context

