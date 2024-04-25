from django.shortcuts import render
from django.http import HttpResponse
from apps.models import Product


def index(request):
    data = {}
    data['dataset'] = Product.objects.all()
    return render(request, "index.html", data)


def about(request):
    return HttpResponse("Salom about bo'limiga xush kelibsiz!")


def contact(request):
    return HttpResponse("Salom contact bo'limiga xush kelibsiz!")


def home(request):
    return HttpResponse("Salom home bo'limiga xush kelibsiz!")
