from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.home, name= 'home'),
    path('phone_detail/<int:id>/', views.phone_detail, name= 'phone_detail'),
]
