from django.contrib import admin
from .models import Property, PropertyImage, PropertyVideo

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'price', 'property_type', 'status', 'is_featured', 'is_new_listing', 'created_at']
    list_filter = ['property_type', 'status', 'is_featured', 'is_new_listing', 'created_at', 'city', 'state']
    search_fields = ['title', 'address', 'city', 'state', 'description']
    list_editable = ['is_featured', 'is_new_listing', 'status']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PropertyImageInline, PropertyVideoInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'property_type', 'status')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Pricing', {
            'fields': ('price',)
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'square_feet', 'lot_size', 'year_built')
        }),
        ('Features', {
            'fields': ('features', 'amenities')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_new_listing')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'caption', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['property__title', 'caption']

@admin.register(PropertyVideo)
class PropertyVideoAdmin(admin.ModelAdmin):
    list_display = ['property', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['property__title', 'title', 'description']
