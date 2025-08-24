from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'inquiry_type', 'property_obj', 'status', 'is_urgent', 'created_at']
    list_filter = ['inquiry_type', 'status', 'is_urgent', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'property_obj__title']
    list_editable = ['status', 'is_urgent']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Inquiry Details', {
            'fields': ('property_obj', 'inquiry_type', 'message')
        }),
        ('Status', {
            'fields': ('status', 'is_urgent', 'contacted_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_contacted', 'mark_as_follow_up', 'mark_as_closed']
    
    def mark_as_contacted(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(status='contacted', contacted_at=timezone.now())
        self.message_user(request, f'{updated} inquiries marked as contacted.')
    mark_as_contacted.short_description = "Mark selected inquiries as contacted"
    
    def mark_as_follow_up(self, request, queryset):
        updated = queryset.update(status='follow_up')
        self.message_user(request, f'{updated} inquiries marked for follow up.')
    mark_as_follow_up.short_description = "Mark selected inquiries for follow up"
    
    def mark_as_closed(self, request, queryset):
        updated = queryset.update(status='closed')
        self.message_user(request, f'{updated} inquiries marked as closed.')
    mark_as_closed.short_description = "Mark selected inquiries as closed"
