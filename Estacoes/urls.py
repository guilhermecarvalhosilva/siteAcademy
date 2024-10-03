from django.urls import path 
from .views import *

app_name = "Estacoes"

urlpatterns = [
    path('', escolher_estacao, name="escolher_estacao" ),
    #roxo
    path('cloud/', cloud, name="cloud"),
    path('low_code/', low_code, name="low_code"),
    #azul
    path('mkt/', mkt, name="mkt"),
    path('sdr/', sdr, name="sdr"),
    #verde 
    path('get/', get, name="get"),
    path('pmo/', pmo, name="pmo"),
    path('qualidade/', qualidade, name="qualidade"),
    #laranja
    path('bpo/', bpo , name="bpo"),
    path('esg/', esg, name="esg"),
    path('rh/', rh, name="rh"),    
]