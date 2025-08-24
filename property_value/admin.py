from django.contrib import admin
from .models import PropertyValue

@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'state', 'formatted_estimated_value', 'formatted_value_range', 'created_at']
    list_filter = ['state', 'city', 'created_at']
    search_fields = ['address', 'city', 'state', 'zip_code', 'contact_name', 'contact_email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Property Information', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'square_feet', 'year_built'),
            'classes': ('collapse',)
        }),
        ('Value Estimates', {
            'fields': ('estimated_value', 'value_range_low', 'value_range_high')
        }),
        ('Market Data', {
            'fields': ('last_sold_price', 'last_sold_date'),
            'classes': ('collapse',)
        }),
        ('Contact Information', {
            'fields': ('contact_name', 'contact_email', 'contact_phone'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
