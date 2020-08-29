from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def market(request):
    return render(request, 'market.html')