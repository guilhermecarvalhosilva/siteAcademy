from django.urls import path
from .views import Sobre, Contato, EscolherEstacao
from django.views.generic import TemplateView, DetailView

app_name = "Core"

urlpatterns = [
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('contato/', Contato.as_view(), name='contato'),
    path('escolher_estacao/', EscolherEstacao.as_view(), name='escolher_estacao'),
    
]
