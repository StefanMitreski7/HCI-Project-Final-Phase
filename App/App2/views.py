import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from pymongo.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from .forms import *

from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def cart(request):
    # Handle cart functionality
    return render(request, 'cart.html')


def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            total_amount = form.cleaned_data['total_amount']
            barcode = form.cleaned_data['barcode']
            delivery_info = form.cleaned_data['delivery_info']

            order = Order.objects.create(
                total_amount=total_amount,
                barcode=barcode,
                delivery_info=delivery_info
            )
            order.products.add(product)

            return redirect('checkout_confirmation')
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form, 'product': product})


def checkout_confirmation(request):
    return render(request, 'checkout_confirmation.html')


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get_or_create(user=request.user)
    user_profile.wishlist.add(product)
    messages.success(request, f"{product.name} added to wishlist.")
    return redirect('product_details', product_id=product_id)


@login_required
def wishlist(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    wishlist_products = user_profile.wishlist.all()
    return render(request, 'wishlist.html', {'wishlist_products': wishlist_products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})


def new(request):
    return render(request, "new.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('product_list')
            else:
                return redirect('product_list')

    return render(request, 'index.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page after creating a product
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})
