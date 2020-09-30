from django.shortcuts import render, redirect
from projects.models import project
from projects.forms import CreateprojectForm
from account.models import Account
from django.contrib import messages
from django.contrib import admin

# Create your views here.
def index(request):
    projects = project.objects.all()
    context = {'projects':projects}
    return render(request,'project/index.html', context)

def createProject(request):
 
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateprojectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        Owner = Account.objects.filter(email=user.email).first()
        obj.Owner = Owner
        obj.save()
        form = CreateprojectForm()
        messages.success(request, 'Project Created')
        

    context['form'] = form
    
    return render(request,"project/create_project.html",context)

