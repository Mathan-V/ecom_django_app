from django.shortcuts import redirect, render
from apv.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.http import *
import json

# Create your views here.
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data =json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            #request.user.id
            product_status = Product.objects.get(id=product_id)
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Alfready in Cart'},status=200)
            else:
                if product_status.quantity>=product_qty:
                    Cart.objects.create(user=request.user.id,product_id=product_id,product_qty=product_qty)
                    return JsonResponse({'status':'Product Added to Cart'},status=200)
                else:
                    return JsonResponse({'status':'Stock Not Available'},status=200)

            return JsonResponse({'status':'Product Added to Cart Success'},status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'},status =200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Loggout Successfully")
    return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,"shop/login.html")

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now..!")
            return redirect('/login')
    return render(request,"shop/register.html",{"form":form})

def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})


def collectionsview(request,name):
    if (Catagory.objects.filter(name=name,status=0)):
        products = Product.objects.filter(catagory__name=name)
        return render(request,"shop/products/index.html",{"products":products,"catagory_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if Catagory.objects.filter(name=cname,status=0):
        if Product.objects.filter(name=pname,status=0):
            products = Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Catagory Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')
