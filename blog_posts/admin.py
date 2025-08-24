from django.contrib import admin
from .models import Category, BlogPost, BlogImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'published_at', 'views', 'created_at']
    list_filter = ['status', 'category', 'published_at', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    list_editable = ['status']
    readonly_fields = ['views', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlogImageInline]
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'featured_image')
        }),
        ('Categorization', {
            'fields': ('author', 'category')
        }),
        ('Publication', {
            'fields': ('status', 'published_at')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('views',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'caption', 'created_at']
    list_filter = ['created_at']
    search_fields = ['post__title', 'caption', 'alt_text']
