from django.contrib import admin
from django.urls import path
from apps.views import index, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('', about, name='about'),
    path('contact', contact, name='contact')
]
