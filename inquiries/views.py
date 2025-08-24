from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Inquiry
from .forms import InquiryForm, ContactForm
from listings.models import Property

# Create your views here.

def contact(request):
    """General contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create inquiry from contact form
            inquiry = Inquiry.objects.create(
                first_name=form.cleaned_data['name'].split()[0] if form.cleaned_data['name'] else '',
                last_name=' '.join(form.cleaned_data['name'].split()[1:]) if len(form.cleaned_data['name'].split()) > 1 else '',
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=f"Subject: {form.cleaned_data['subject']}\n\n{form.cleaned_data['message']}",
                inquiry_type='general'
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('inquiries:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'inquiries/contact.html', context)

def submit_inquiry(request):
    """Submit a general inquiry"""
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            messages.success(request, 'Thank you for your inquiry! We will contact you soon.')
            return redirect('listings:home')
    else:
        form = InquiryForm()
    
    context = {
        'form': form,
    }
    return render(request, 'inquiries/submit_inquiry.html', context)

def property_inquiry(request, property_id):
    """Submit an inquiry for a specific property"""
    property_obj = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property_obj = property_obj
            inquiry.inquiry_type = 'buy' if property_obj.status == 'for_sale' else 'rent'
            inquiry.save()
            messages.success(request, 'Thank you for your interest! We will contact you soon about this property.')
            return redirect('listings:property_detail', property_id=property_id)
    else:
        form = InquiryForm()
    
    context = {
        'form': form,
        'property': property_obj,
    }
    return render(request, 'inquiries/property_inquiry.html', context)
