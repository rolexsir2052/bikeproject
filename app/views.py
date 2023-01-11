from django.shortcuts import render,redirect
from app.forms import *
from django.views.generic import View,TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
def dummy(request):
    return render(request,'dummyr.html')
@login_required(login_url='login_user')
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        N=request.POST.get('n')
        P=request.POST.get('p')
        U=User.objects.create_user(username=N,password=P)
        U.save()
        return redirect('home')
    return render(request,'register.html')
def contact(request):
    return render(request,'contact.html')
def login_user(request):    
    if request.method=='POST':
        N=request.POST.get('n')
        P=request.POST.get('p')
        user=authenticate(username=N,password=P)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login_user')
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('login_user')
        
