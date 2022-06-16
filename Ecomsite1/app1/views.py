from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone

# Create your views here.
def home(request):
    phone = Phone.objects.all()
    context = {
    'phone' : phone
    }
    return render(request, 'app1/index.html', context)

def phone_detail(request,id):
    phone = Phone.objects.get(id=id)
    context = {
    'phone' : phone
    }
    return render(request, 'app1/phone_detail.html', context)

