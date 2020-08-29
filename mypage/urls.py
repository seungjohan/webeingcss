from django.contrib import admin
from django.urls import path, include
import mypage.views

urlpatterns = [
    path('/myinformation', mypage.views.myinformation, name="myinformation"),
    path('/orderlist', mypage.views.orderlist, name="orderlist"),
    path('/account', mypage.views.account, name="account"),
]

