from django.shortcuts import render

# Create your views here.

def accountconnect(request):
    return render(request, 'accountconnect.html')

def goods(request):
    return render(request, 'goods.html')