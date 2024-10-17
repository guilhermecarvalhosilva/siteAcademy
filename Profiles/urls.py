from django.urls import path
from .views import *

app_name = 'Profiles'


urlpatterns = [
    path('login/', login_view, name='login'),
]
