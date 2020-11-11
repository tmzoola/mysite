from django.shortcuts import render
from django.http import HttpResponse

from .models import *



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {'orders':orders, 'customers':customers}
    return render(request, 'web/dashboard.html', context)

def products(request):
    product = Products.objects.all()
    return render(request, 'web/products.html', {'products':product})

def customer(request):
    return render(request, 'web/customer.html')