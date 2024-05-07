from django.shortcuts import render, redirect
from apps.models import Product, Post
from apps.forms import ContactForm


def index(request):
    data = {}
    data['dataset'] = Product.objects.all()
    return render(request, "index.html", data)


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'GET':
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context)
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'contact.html', {'form': form})


def home(request):
    return render(request, 'homepage.html')


def news(request):
    posts = {}
    posts["dataset"] = Post.objects.all()
    return render(request, 'news.html', context=posts)


def blog(request):
    return render(request, "Blog.html")


def blog2(request):
    post = {}
    post["dataset"] = Post.objects.all()
    return render(request, "Blog2.html", post)
