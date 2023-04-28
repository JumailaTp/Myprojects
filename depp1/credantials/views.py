from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info("invalid credentials")
            return redirect('/')
    return render(request, "login.html")
def register(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password1']
        confirmpass=request.POST['password2']

        if password==confirmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                messages.info(request, "user created")
                # print("user created")
                return render(request,"login.html")
        else:
                messages.info(request,"password not matched")
                return render(request,"register.html")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')



# Create your views here.
