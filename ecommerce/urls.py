"""ecommerce URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from avatar.views import CustomSignupView


urlpatterns = [
    path(
        'admin/', admin.site.urls),
    path(
        "accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path(
        'accounts/', include('allauth.urls')),
    path(
        '', include('home.urls')),
    path(
        'about/', include('about.urls')),
    path(
        'blog/', include('blog.urls')),
    path(
        'products/', include('products.urls')),
    path(
        'bag/', include('bag.urls')),
    path(
        'checkout/', include('checkout.urls')),
    path(
        'profile/', include('profiles.urls')),
    path(
        'avatar/', include('avatar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ecommerce.views.handler404'
