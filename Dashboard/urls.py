from django.urls import path 
from .views import Dashboard, Base


urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('base/', Base.as_view(), name="save"),
]