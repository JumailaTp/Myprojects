from django.http import HttpResponse
from django.shortcuts import render
from .models import place,Team
# Create your views here.
def demo(request):
    # name="india"
    obj=place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj1})
# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     sub1=x-y
#     mul1=x*y
#     div1=x/y
#     return render(request,"result.html",{'result':res,'substraction':sub1,'multiplication':mul1,'division':div1})
# def contact(request):
#     return HttpResponse("iam contact")