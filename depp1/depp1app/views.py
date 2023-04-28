from django.shortcuts import render
from .models import place,Team
# Create your views here.
def demo(request):
    # name="india"
    obj=place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj1})
