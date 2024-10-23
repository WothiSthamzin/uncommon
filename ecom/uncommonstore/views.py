from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

def search(request):
    """Render the search results page."""
    return render(request, "search.html", {})

def category_summary(request):
    """Display a summary for all categories"""
    categories = Category.objects.all()
    return render(request, "category_summary.html", {'categories':categories})

def category(request,foo):
    """
    Display products within a specific category.

    Args:
        request: The HTTP request object.
        foo (str): The category name (with hyphens replaced by spaces).

    Returns:
        Rendered category page with products or redirects to home if the category doesn't exist.
    """
    foo = foo.replace('_', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})

    except:
        messages.success(request, ("That Category Doesn't Exist."))
        return redirect('home')


def product(request,pk):
    """Display a specific product based on its primary key."""
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    """Display the home page with all products."""
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    """Render the about page."""
    return render(request, 'about.html', {})

def login_user(request):
    """
    Handle user login.

    Args:
        request: The HTTP request object.

    Returns:
        Redirect to home on successful login or re-render login page with error message.
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('home')

        else:
            messages.success(request, ("There Was An Error, Please Try Again."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    """Handle user logout and redirect to home."""
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home')

def register_user(request):
    """
    Handle user registration.

    Args:
        request: The HTTP request object.

    Returns:
        Redirect to login page after successful registration or re-render registration page with form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm
    return render(request, 'register.html', {"form":form})