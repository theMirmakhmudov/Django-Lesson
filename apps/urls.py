from django.contrib import admin
from django.urls import path
from apps.views import index, about, contact, home, new, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('home', home, name='homepage'),
    path('news', new, name='new'),
    path('', blog, name='blog'),
]
