from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('homehome/', home.views.home, name = "home"),
    path('market/', home.views.market, name = "market"),

    
]
