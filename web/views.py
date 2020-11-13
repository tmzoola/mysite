from django.shortcuts import render
from django.http import HttpResponse

from .models import *



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pendings = orders.filter(status='Pending').count()


    context = {'orders':orders,
               'customers':customers,
               'total_orders':total_orders,
               'total_customers':total_customers,
               'delivered':delivered,
               'pendings':pendings
               }
    return render(request, 'web/dashboard.html', context)



def products(request):
    product = Products.objects.all()
    return render(request, 'web/products.html', {'products':product})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()

    context = {'customer':customer, 'orders':orders}

    return render(request, 'web/customer.html', context)