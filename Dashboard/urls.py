from django.urls import path 
from .views import IndexDashboardView, ListEstacaoView


urlpatterns = [
    path('', IndexDashboardView.as_view(), name="index_estacao"),
    path('listar_projetos/', ListEstacaoView.as_view(), name="list_estacao"),
]