from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username/password")
            return redirect('login')
    return render(request,"login.html")
def regester(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password not match")
            return redirect('register')
        return redirect('/')

    return render(request,"regester.html")

def logout(request):
    auth.logout(request)
    return redirect('/')