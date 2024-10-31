from django.shortcuts import render
from django.views.generic import ListView
from .models import Projeto

# Create your views here.
class Dashboard(ListView):
    template_name = "dashboard.html"
    model = Projeto
    context_object_name = "projetos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projetos'] = range(50)
        return context

class Base(ListView):
    template_name = "save.html"
    model = Projeto
    context_object_name = "projetos"