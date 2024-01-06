from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"shop/index.html")
def register(request):
    return render(request,"shop/register.html")
def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})


def collectionsview(request,name):
    if (Catagory.objects.filter(name=name,status=0)):
        products = Product.objects.filter(catagory__name=name)
        return render(request,"shop/products/index.html",{"products":products})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')
