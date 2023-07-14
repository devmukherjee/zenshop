from django.shortcuts import render
from .models import Product,Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects= Product.objects.all()
    item_name= request.GET.get("item_name")

    #Search code 
    if item_name!="" and item_name is not None:
        product_objects= Product.objects.filter(title__icontains= item_name)

    #Pagination code
    paginator= Paginator(product_objects,4)
    page= request.GET.get('page')
    product_objects= paginator.get_page(page)

    return render(request,'shop/index.html',{"product_objects":product_objects})


def detail(request,id):
    product_object= Product.objects.get(pk= id)

    return render(request,'shop/detail.html',{"product_object":product_object})

def checkout(request):
    if(request.method=="POST"):
        items= request.POST.get("items")
        name= request.POST.get("name")
        email= request.POST.get("email")
        address= request.POST.get("address")
        city= request.POST.get("city")
        state= request.POST.get("state")
        zipcode= request.POST.get("zipcode")
        total=request.POST.get("total")
        order= Order(name= name,email=email,address=address,state=state,city= city,zipcode=zipcode,items=items,total= total)
        order.save()
    return render(request,'shop/checkout.html')
