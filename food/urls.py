from django.contrib import admin
from django.urls import path, include
import food.views

urlpatterns = [
    path('food/', food.views.order, name="order"),
]
