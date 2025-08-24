from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('buy/', views.buy_home, name='buy_home'),
    path('sell/', views.sell_home, name='sell_home'),
    path('featured/', views.featured_listings, name='featured_listings'),
    path('new/', views.new_listings, name='new_listings'),
    
    # Property details
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    
    # Search and filters
    path('search/', views.property_search, name='property_search'),
    path('filter/', views.property_filter, name='property_filter'),
    
    # Property types
    path('type/<str:property_type>/', views.property_by_type, name='property_by_type'),
    
    # Location based
    path('location/<str:city>/', views.property_by_location, name='property_by_location'),
]
