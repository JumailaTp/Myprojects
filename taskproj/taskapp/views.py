from django.shortcuts import render

# Create your views here.
def demo(request):
    # name="india"

    return render(request,"index.html")