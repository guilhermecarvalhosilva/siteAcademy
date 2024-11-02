from django.urls import path 
from .views import List_estacao, Index_dashboard, Base


urlpatterns = [
    path('', Index_dashboard.as_view(), name="index_estacao"),
    path('visualizar/<int:pk>', List_estacao.as_view(), name="list_estacao"),
    path('menu_lateral/', Base.as_view(), name="base"),
]