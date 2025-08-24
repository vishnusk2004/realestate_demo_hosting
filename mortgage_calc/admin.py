from django.contrib import admin
from .models import MortgageCalculation

@admin.register(MortgageCalculation)
class MortgageCalculationAdmin(admin.ModelAdmin):
    list_display = ['formatted_property_price', 'loan_term_years', 'interest_rate', 'formatted_monthly_payment', 'loan_type', 'created_at']
    list_filter = ['loan_type', 'loan_term_years', 'created_at']
    search_fields = ['contact_name', 'contact_email', 'contact_phone']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Property Information', {
            'fields': ('property_price', 'down_payment', 'down_payment_percentage')
        }),
        ('Loan Information', {
            'fields': ('loan_amount', 'interest_rate', 'loan_term_years', 'loan_type')
        }),
        ('Monthly Payments', {
            'fields': ('monthly_principal_interest', 'monthly_property_tax', 'monthly_insurance', 'monthly_pmi', 'total_monthly_payment')
        }),
        ('Total Costs', {
            'fields': ('total_interest_paid', 'total_payment')
        }),
        ('Contact Information', {
            'fields': ('contact_name', 'contact_email', 'contact_phone'),
            'classes': ('collapse',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
