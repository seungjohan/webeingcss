from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('/home', home.views.home, name = "home.html"),
    path('/market', home.views.market, name = "market.html")

    
]
