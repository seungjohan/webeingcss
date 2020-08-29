from django.shortcuts import render

# Create your views here.

def myinformation(request):
    return render(request, 'myinformation.html')

def orderlist(request):
    return render(request, 'orderlist.html')

def account(request):
    return render(request, 'account.html')
