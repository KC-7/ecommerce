from django.urls import path
from . import views

urlpatterns = [
    path('create_punk/', views.generate_and_save_punk_for_user, name='create_punk'),
]
