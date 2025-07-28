# apps/landing/views.py
from django.shortcuts import render

def landing_page(request):
    # Halaman sederhana
    return render(request, 'landing/landing_page.html')

def product_page(request):
    # Halaman dengan data dari Python
    context = {
        'nama': 'Slayer',
        'produk': ['Laptop', 'Keyboard', 'Mouse']
    }
    return render(request, 'landing/index.html', context)
