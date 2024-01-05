from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    return render(request,"shop/index.html")
def register(request):
    return render(request,"shop/register.html")
def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})
