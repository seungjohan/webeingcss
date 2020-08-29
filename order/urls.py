from django.contrib import admin
from django.urls import path
import order.views


urlpatterns = [
    path('complete/', order.views.order, name = "order"),
    path('complete/', order.views.complete, name = "complete"),
]
