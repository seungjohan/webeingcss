from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def signupseller(request):
    return render(request, 'signupseller.html')

def signupintro(request):
    return render(request, 'signupintro.html')