from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.
def search(request):
    return render(request, "search.html", {})

def category_summary(request):
    categories = Category.objects.all()
    return render(request, "category_summary.html", {'categories':categories})

def category(request,foo):
    # Replacing Hyphens with spaces
    foo = foo.replace('_', ' ')
    # 'Category' from 'url'
    try:
        # Call Up 'Category'
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})

    # If 'Category' doesn't exist
    except:
        messages.success(request, ("That Category Doesn't Exist."))
        return redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    # For logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # To 'authenticate'
        user = authenticate(request, username=username, password=password)
        # If 'username' is not blank
        if user is not None:
            # PASS IN
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('home')

        # If authentication is not successful
        else:
            messages.success(request, ("There Was An Error, Please Try Again."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home')

def register_user(request):
    # For 'form' submission :
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # If 'form' is valid, user will be saved/registered
        if form.is_valid():
            form.save()
            # Once registered, user will be redirected to homepage
            return redirect('login')
    # For empty form
    else:
        form = UserCreationForm
    # If 'form' is not valid
    return render(request, 'register.html', {"form":form})