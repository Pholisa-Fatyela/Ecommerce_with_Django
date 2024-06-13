#from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>My First Webpage with Python Django<h1>")
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'Ecommerce/product_list.html',context)
