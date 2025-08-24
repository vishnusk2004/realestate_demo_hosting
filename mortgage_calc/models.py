from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class MortgageCalculation(models.Model):
    LOAN_TYPES = [
        ('conventional', 'Conventional'),
        ('fha', 'FHA'),
        ('va', 'VA'),
        ('usda', 'USDA'),
    ]
    
    # Property information
    property_price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    down_payment = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    down_payment_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Loan information
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    interest_rate = models.DecimalField(max_digits=5, decimal_places=3, validators=[MinValueValidator(0)])
    loan_term_years = models.PositiveIntegerField()
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES, default='conventional')
    
    # Monthly payments
    monthly_principal_interest = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    monthly_property_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_insurance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_pmi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Total costs
    total_interest_paid = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    total_payment = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Contact information (optional)
    contact_name = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"${self.property_price:,.2f} - {self.loan_term_years}yr - {self.interest_rate}%"
    
    @property
    def formatted_property_price(self):
        return f"${self.property_price:,.2f}"
    
    @property
    def formatted_monthly_payment(self):
        return f"${self.total_monthly_payment:,.2f}"
    
    @property
    def formatted_total_interest(self):
        return f"${self.total_interest_paid:,.2f}"
