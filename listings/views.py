from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Property
from inquiries.forms import InquiryForm
from blog_posts.models import BlogPost

def home(request):
    """Home page view"""
    featured_properties = Property.objects.filter(is_featured=True, status='for_sale')[:8]
    blog_posts = BlogPost.objects.filter(status='published').order_by('-published_at')[:3]
    
    context = {
        'featured_properties': featured_properties,
        'blog_posts': blog_posts,
    }
    return render(request, 'listings/home.html', context)

def buy_home(request):
    """Buy a home page"""
    properties = Property.objects.filter(status='for_sale').order_by('-created_at')
    
    # Filter by property type
    property_type = request.GET.get('property_type')
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    # Filter by location
    location = request.GET.get('location')
    if location:
        properties = properties.filter(
            Q(city__icontains=location) | 
            Q(state__icontains=location) | 
            Q(zip_code__icontains=location)
        )
    
    # Filter by price range
    price_range = request.GET.get('price_range')
    if price_range:
        if price_range == '0-200000':
            properties = properties.filter(price__lte=200000)
        elif price_range == '200000-400000':
            properties = properties.filter(price__gte=200000, price__lte=400000)
        elif price_range == '400000-600000':
            properties = properties.filter(price__gte=400000, price__lte=600000)
        elif price_range == '600000-800000':
            properties = properties.filter(price__gte=600000, price__lte=800000)
        elif price_range == '800000-1000000':
            properties = properties.filter(price__gte=800000, price__lte=1000000)
        elif price_range == '1000000+':
            properties = properties.filter(price__gte=1000000)
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
        'property_types': Property.PROPERTY_TYPES,
    }
    return render(request, 'listings/buy_home.html', context)

def sell_home(request):
    """Sell a home page"""
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.inquiry_type = 'sell'
            inquiry.save()
            messages.success(request, 'Thank you for your inquiry! We will contact you soon.')
            return redirect('listings:sell_home')
    else:
        form = InquiryForm()
    
    context = {
        'form': form,
    }
    return render(request, 'listings/sell_home.html', context)

def featured_listings(request):
    """Featured listings page"""
    properties = Property.objects.filter(is_featured=True, status='for_sale').order_by('-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
    }
    return render(request, 'listings/featured_listings.html', context)

def new_listings(request):
    """New listings page"""
    properties = Property.objects.filter(is_new_listing=True, status='for_sale').order_by('-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
    }
    return render(request, 'listings/new_listings.html', context)

def property_detail(request, property_id):
    """Property detail page"""
    property_obj = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property_obj = property_obj
            inquiry.inquiry_type = 'buy'
            inquiry.save()
            messages.success(request, 'Thank you for your inquiry! We will contact you soon.')
            return redirect('listings:property_detail', property_id=property_id)
    else:
        form = InquiryForm()
    
    # Get related properties
    related_properties = Property.objects.filter(
        Q(city=property_obj.city) | Q(property_type=property_obj.property_type),
        status='for_sale'
    ).exclude(id=property_obj.id)[:3]
    
    context = {
        'property': property_obj,
        'form': form,
        'related_properties': related_properties,
    }
    return render(request, 'listings/property_detail.html', context)

def property_search(request):
    """Property search page"""
    properties = Property.objects.filter(status='for_sale')
    
    # Get search parameters
    property_type = request.GET.get('property_type')
    location = request.GET.get('location')
    price_range = request.GET.get('price_range')
    
    # Apply filters
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    if location:
        properties = properties.filter(
            Q(city__icontains=location) | 
            Q(state__icontains=location) | 
            Q(zip_code__icontains=location)
        )
    
    if price_range:
        if price_range == '0-200000':
            properties = properties.filter(price__lte=200000)
        elif price_range == '200000-400000':
            properties = properties.filter(price__gte=200000, price__lte=400000)
        elif price_range == '400000-600000':
            properties = properties.filter(price__gte=400000, price__lte=600000)
        elif price_range == '600000-800000':
            properties = properties.filter(price__gte=600000, price__lte=800000)
        elif price_range == '800000-1000000':
            properties = properties.filter(price__gte=800000, price__lte=1000000)
        elif price_range == '1000000+':
            properties = properties.filter(price__gte=1000000)
    
    # Sort by created date
    properties = properties.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
        'property_types': Property.PROPERTY_TYPES,
        'search_params': {
            'property_type': property_type,
            'location': location,
            'price_range': price_range,
        }
    }
    return render(request, 'listings/property_search.html', context)

def property_filter(request):
    """Property filter page"""
    properties = Property.objects.filter(status='for_sale')
    
    # Get filter parameters
    property_type = request.GET.get('property_type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
    
    # Apply filters
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    if min_price:
        properties = properties.filter(price__gte=min_price)
    
    if max_price:
        properties = properties.filter(price__lte=max_price)
    
    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)
    
    if bathrooms:
        properties = properties.filter(bathrooms__gte=bathrooms)
    
    # Sort by created date
    properties = properties.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
        'property_types': Property.PROPERTY_TYPES,
    }
    return render(request, 'listings/property_filter.html', context)

def property_by_type(request, property_type):
    """Properties by type"""
    properties = Property.objects.filter(
        property_type=property_type, 
        status='for_sale'
    ).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
        'property_type': property_type,
        'property_types': Property.PROPERTY_TYPES,
    }
    return render(request, 'listings/property_by_type.html', context)

def property_by_location(request, location):
    """Properties by location"""
    properties = Property.objects.filter(
        Q(city__icontains=location) | 
        Q(state__icontains=location) | 
        Q(zip_code__icontains=location),
        status='for_sale'
    ).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'properties': page_obj,
        'location': location,
    }
    return render(request, 'listings/property_by_location.html', context)
