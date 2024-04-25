from django.shortcuts import render
from django.http import HttpResponse
from apps.models import Product


def index(request):
    data = {}
    data['dataset'] = Product.objects.all()
    return render(request, "index.html", data)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def home(request):
    return render(request, 'homepage.html')
