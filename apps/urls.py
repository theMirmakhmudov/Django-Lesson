from django.contrib import admin
from django.urls import path
from apps.views import index, about, contact, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('', home, name='homepage')
]
