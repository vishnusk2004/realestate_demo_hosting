from django.db import models

class Inquiry(models.Model):
    INQUIRY_TYPES = [
        ('buy', 'Buy'),
        ('rent', 'Rent'),
        ('sell', 'Sell'),
        ('general', 'General'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('follow_up', 'Follow Up'),
        ('closed', 'Closed'),
    ]
    
    # Contact information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Property information
    property_obj = models.ForeignKey('listings.Property', on_delete=models.CASCADE, null=True, blank=True)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES, default='general')
    
    # Message
    message = models.TextField()
    
    # Status and tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    is_urgent = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Inquiries'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.inquiry_type} - {self.created_at.strftime('%Y-%m-%d')}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def is_new(self):
        return self.status == 'new'
