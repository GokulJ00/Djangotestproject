from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def test_fun(request):
    return render(request, 'test.html')


def test_func(request):
    return render(request, 'home.html')