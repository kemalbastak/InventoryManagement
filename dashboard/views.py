from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
    }
    return render(request, "dashboard/home.html", context)

@login_required(login_url='login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers,
    }
    return render(request, "dashboard/staff.html", context)

@login_required(login_url='login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    print(workers.profile.image.url)
    context = {
        'worker': workers,
    }
    return render(request, "dashboard/staff_detail.html", context)


@login_required(login_url='login')
def products(request):
    items = Product.objects.all()
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('products')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, "dashboard/products.html", context)

@login_required(login_url='login')
def products_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

@login_required(login_url='login')
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
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, "dashboard/order.html", context)
