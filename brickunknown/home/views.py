from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        comment = request.POST.get('comment')
        contact = Contact(name=name,email=email,mob=mob,comment=comment,
        date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent')
    return render(request,"index.html")