from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import BlogPost, Category

def blog_list(request):
    """Blog listing page"""
    posts = BlogPost.objects.filter(status='published').order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get categories for sidebar
    categories = Category.objects.all()
    
    context = {
        'posts': page_obj,
        'categories': categories,
    }
    return render(request, 'blog_posts/blog_list.html', context)

def blog_detail(request, slug):
    """Individual blog post detail page"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    
    # Increment view count
    post.views += 1
    post.save()
    
    # Get related posts
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog_posts/blog_detail.html', context)

def blog_by_category(request, slug):
    """Blog posts filtered by category"""
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(
        category=category,
        status='published'
    ).order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get categories for sidebar
    categories = Category.objects.all()
    
    context = {
        'posts': page_obj,
        'category': category,
        'categories': categories,
    }
    return render(request, 'blog_posts/blog_by_category.html', context)

def blog_by_author(request, username):
    """Blog posts filtered by author"""
    author = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(
        author=author,
        status='published'
    ).order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'author': author,
    }
    return render(request, 'blog_posts/blog_by_author.html', context)
