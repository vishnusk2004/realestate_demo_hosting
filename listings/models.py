from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]
    
    STATUS_CHOICES = [
        ('for_sale', 'For Sale'),
        ('for_rent', 'For Rent'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='for_sale')
    
    # Property details
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    square_feet = models.PositiveIntegerField(default=0)
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    
    # Features
    features = models.TextField(blank=True)
    amenities = models.TextField(blank=True)
    
    # Images and media
    main_image = models.ImageField(upload_to='properties/main/', null=True, blank=True)
    
    # Meta information
    is_featured = models.BooleanField(default=False)
    is_new_listing = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Properties'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.address}"
    
    @property
    def formatted_price(self):
        return f"${self.price:,.2f}"
    
    @property
    def main_image_url(self):
        """Return main image URL or placeholder"""
        if self.main_image:
            return self.main_image.url
        # Return different placeholder images for variety - more luxurious and welcoming
        placeholders = [
            'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400&h=300&fit=crop',  # Luxury modern home
            'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=300&fit=crop',  # Cozy family home
            'https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=400&h=300&fit=crop',  # Elegant interior
            'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=400&h=300&fit=crop',  # Beautiful exterior
            'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=400&h=300&fit=crop',  # Modern architecture
            'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',  # Contemporary home
        ]
        # Use property ID to consistently assign the same image to each property
        return placeholders[self.id % len(placeholders)] if self.id else placeholders[0]

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/images/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_primary', 'created_at']
    
    def __str__(self):
        return f"{self.property.title} - {self.caption or 'Image'}"

class PropertyVideo(models.Model):
    property = models.ForeignKey(Property, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='properties/videos/', null=True, blank=True)
    video_url = models.URLField(blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.property.title} - {self.title}"
