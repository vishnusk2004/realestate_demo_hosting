from django.db import models
from django.core.validators import MinValueValidator

class PropertyValue(models.Model):
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    # Estimated values
    estimated_value = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    value_range_low = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    value_range_high = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Property details (if available)
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    square_feet = models.PositiveIntegerField(null=True, blank=True)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    
    # Market data
    last_sold_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    last_sold_date = models.DateField(null=True, blank=True)
    
    # Contact information for follow-up
    contact_name = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Property Values'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.address} - ${self.estimated_value:,.2f}"
    
    @property
    def full_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
    
    @property
    def formatted_estimated_value(self):
        return f"${self.estimated_value:,.2f}"
    
    @property
    def formatted_value_range(self):
        return f"${self.value_range_low:,.2f} - ${self.value_range_high:,.2f}"
