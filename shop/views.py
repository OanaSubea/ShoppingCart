# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Category
from .models import Product

def home(request):
    return render(request, "main/home.html",{'message':'Hi, there!'})#main-ul din templates

def product_list(request):
    #if request.method == 'GET':
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories:': categories, #este un dictionar, doar cu dictionar functioneaza
        'products': products,
    }
    return render(request, 'shop/list.html', context)

