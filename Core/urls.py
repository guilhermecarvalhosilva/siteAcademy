from django.urls import path 
from .views import *

app_name = "Core"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('contato/', contato, name="contato"),
    path('sobre/', sobre, name="sobre"),
    path('cadastro/', sobre, name="cadastro"),
    path('login/', sobre, name="login"),

]