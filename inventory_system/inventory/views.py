from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Supplier, SaleOrder, StockMovement
from .forms import ProductForm, SupplierForm, SaleOrderForm, StockMovementForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'inventory/list_products.html', {'products': products})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_suppliers')
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})

def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/list_suppliers.html', {'suppliers': suppliers})

def add_stock_movement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            movement = form.save()
            product = movement.product
            if movement.movement_type == 'In':
                product.stock_quantity += movement.quantity
            elif movement.movement_type == 'Out' and product.stock_quantity >= movement.quantity:
                product.stock_quantity -= movement.quantity
            product.save()
            return redirect('list_products')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/add_stock_movement.html', {'form': form})

def create_sale_order(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            product = order.product
            if product.stock_quantity >= order.quantity:
                order.total_price = product.price * order.quantity
                product.stock_quantity -= order.quantity
                product.save()
                order.save()
                return redirect('list_sale_orders')
            else:
                form.add_error('quantity', 'Insufficient stock!')
    else:
        form = SaleOrderForm()
    return render(request, 'inventory/create_sale_order.html', {'form': form})

def list_sale_orders(request):
    orders = SaleOrder.objects.all()
    return render(request, 'inventory/list_sale_orders.html', {'orders': orders})
