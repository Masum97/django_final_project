from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def staff(request):

    return render(request, 'dashboard/staff.html')


def product(request):
    items = Product.objects.all()
    #items = Product.objects.raw('SELECT *FROM dashboard_product')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')

    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)


def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


def profile(request):
    return render(request, 'user/profile.html')


def order(request):
    return render(request, 'dashboard/order.html')
