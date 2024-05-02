from django.shortcuts import render
from apps.models import Product, Post


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


def new(request):
    posts = {}
    posts["posts"] = Post.objects.all()
    return render(request, 'new.html', posts)


def blog(request):
    return render(request, "Blog.html")


def blog2(request):
    post = {}
    post["dataset"] = Post.objects.all()
    return render(request, "Blog2.html", post)
