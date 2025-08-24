from django.urls import path
from . import views

app_name = 'property_value'

urlpatterns = [
    path('', views.home_value, name='home_value'),
    path('estimate/', views.estimate_value, name='estimate_value'),
]
