from django.urls import path 
from .views import IndexDashboardView, DetalhesProjetosEstacoes


urlpatterns = [
    path('', IndexDashboardView.as_view(), name="index_estacao"),
    path('listar_projetos/<str:nome>/', DetalhesProjetosEstacoes.as_view(), name="list_estacao"),
]