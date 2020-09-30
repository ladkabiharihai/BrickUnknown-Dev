from django.shortcuts import render,HttpResponse
from hireus.models import Product
from datetime import datetime
from hireus.models import booked
from django.contrib import messages
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"hireus/index.html", context)

def bookorder(request): 
    return render(request,"hireus/bookorder.html")


def Booked(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        details = request.POST.get('details')
        category = request.POST.get('category')
        Product_name = request.POST.get('Product_name')
        Booked = booked(name=name,email=email,mob=mob,details=details,date=datetime.today(),Product_name=Product_name,category=category)
        Booked.save()
        messages.success(request, 'your order has been booked')
    return render(request,"hireus/bookorder.html")


def productview(request, Product_id):
    product = Product.objects.filter(Product_id=Product_id)
    return render(request,"hireus/detail_view.html",{'product':product[0]})
