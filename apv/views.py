from django.shortcuts import redirect, render
from apv.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.http import HttpResponse 

# Create your views here.
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

def login(request):
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
