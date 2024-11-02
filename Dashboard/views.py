from django.shortcuts import render
from django.views.generic import ListView
from .models import Projeto

# Create your views here.
class List_estacao(ListView):
    template_name = "list_dashboard.html"
    model = Projeto
    context_object_name = "projetos"


class Index_dashboard(ListView):
    template_name = "index_dashboard.html"
    model = Projeto
    context_object_name = "projetos"


class Base(ListView):
    template_name = "bases/menu_lateral.html"
    model = Projeto
    context_object_name = "projetos"
