from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, "dashboard/home.html")

@login_required(login_url='login')
def staff(request):
    return render(request, "dashboard/staff.html")

@login_required(login_url='login')
def products(request):
    items = Product.objects.all()
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, "dashboard/products.html", context)

def products_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

def products_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=item)
    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)

@login_required(login_url='login')
def order(request):
    return render(request, "dashboard/order.html")
