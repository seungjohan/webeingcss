from django.contrib import admin
from django.urls import path, include
import landing.views

urlpatterns = [
    path('', landing.views.landing, name="landing"),
]
