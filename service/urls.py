from django.contrib import admin
from django.urls import path, include
import service.views


urlpatterns = [
    path('accountconnect/', service.views.accountconnect, name="accountconnect"),
    path('goods/', service.views.goods, name = "goods"),
]
