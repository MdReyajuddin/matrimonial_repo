from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def starter(request):
    return render(request,'starter.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['passwordagain']:
            try:
                user = User.objects.get(username =request.POST['username'])
                return render(request, 'registration.html', {'error': "User Already Exists"})
            except User.DoesNotExist:
                user =User.objects.create_user(username= request.POST['username'],password= request.POST['password'])
                return redirect(starter)
        else:
            return render(request,'registration.html',{'error':"Password Doesnot Matched"})
    else:
        return render(request,'registration.html')


def login(request):
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request, 'home.html')
        else:
            return render(request,'starter.html',{'error':"Invalid Login Credentials"})
    else:
        return render(request, 'starter.html')


def logout(request):
    auth.logout(request)
    return redirect(starter)
