from django.urls import path
from . import views

app_name = 'inquiries'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('submit/', views.submit_inquiry, name='submit_inquiry'),
    path('property/<int:property_id>/', views.property_inquiry, name='property_inquiry'),
]
