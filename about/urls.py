from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('create/', views.create_about_page, name='create_about_page'),
    path('<int:pk>/', views.about_page_detail, name='about_page_detail'),
    path('<int:pk>/delete/', views.delete_about_page, name='delete_about_page'),
    path('<int:pk>/edit/', views.edit_about_page, name='edit_about_page'),
]
