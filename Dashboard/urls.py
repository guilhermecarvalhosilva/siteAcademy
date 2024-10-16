from django.urls import path 
from .views import *

app_name = "Dashboard"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('base/', base, name="base"),
]