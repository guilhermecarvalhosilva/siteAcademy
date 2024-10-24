from django.urls import path
from .views import Sobre, Contato, DetalhesEstacaoView


app_name = "Core"

urlpatterns = [
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('contato/', Contato.as_view(), name='contato'),
    path('estacoes/<int:pk>', DetalhesEstacaoView.as_view(), name='estacoes'),
    
]
