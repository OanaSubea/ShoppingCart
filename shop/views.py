# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Category
from .models import Product

def home(request):
    return render(request, "main/home.html",{'message':'Hi, there!'})#main-ul din templates

#def product_lits(request):
 #   if request.method == 'GET':

