# apps/landing/urls.py
from django.urls import path
from .views import landing_page, product_page

urlpatterns = [
    path('', landing_page, name='landing'),
    path('produk/', product_page, name='produk'),
]
