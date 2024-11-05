from django.urls import path
from .views import Sobre, Contato, DetalhesEstacaoView, Desenvolvedores, TesteView


app_name = "Core"

urlpatterns = [
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('contato/', Contato.as_view(), name='contato'),
    path('estacao/<str:nome>/', DetalhesEstacaoView.as_view(), name='detalhes_estacao'),
    path('desenvolvedores/', Desenvolvedores.as_view(), name='desenvolvedores'),
    path('teste/<str:nome>/', TesteView.as_view(), name='teste_view'),
]
