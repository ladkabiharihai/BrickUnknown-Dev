from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    
    return render(request,"hireus/index.html")

def cart(request):
    
    return render(request,"hireus/cart.html")

def checkout(request):
    
    return render(request,"hireus/checkout.html")

