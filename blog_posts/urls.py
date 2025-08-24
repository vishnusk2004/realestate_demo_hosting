from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.blog_by_category, name='blog_by_category'),
    path('author/<str:username>/', views.blog_by_author, name='blog_by_author'),
]
