from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def reg(request):
    return render(request, 'main/reg.html')

def auto(request):
    return render(request, 'main/auto.html')

def about(request):
    return render(request, 'main/about.html')