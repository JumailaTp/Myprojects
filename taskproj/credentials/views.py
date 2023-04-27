from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request, "new.html")

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
                return render(request,"register.html")

            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                print("user created")
                return render(request,"register.html")
        else:
                messages.info(request,"password not matched")
                return render(request,"register.html")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def formm(request):
    return render(request,"formm.html")





def accept(request):
    messages.info(request," application accepted")
    return render(request,"formm.html")


def home(request):
    return render(request,"index.html")
