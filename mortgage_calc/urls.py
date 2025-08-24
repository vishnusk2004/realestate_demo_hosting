from django.urls import path
from . import views

app_name = 'mortgage'

urlpatterns = [
    path('', views.mortgage_calculator, name='mortgage_calculator'),
    path('calculate/', views.calculate_mortgage, name='calculate_mortgage'),
]
