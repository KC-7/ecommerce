from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create/', views.create_blog_page, name='create_blog_page'),
    path('<int:pk>/', views.blog_page_detail, name='blog_page_detail'),
    path('<int:pk>/delete/', views.delete_blog_page, name='delete_blog_page'),
    path('<int:pk>/edit/', views.edit_blog_page, name='edit_blog_page'),
]
