from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'web/dashboard.html')

def products(request):
    return render(request, 'web/products.html')

def customer(request):
    return render(request, 'web/customer.html')