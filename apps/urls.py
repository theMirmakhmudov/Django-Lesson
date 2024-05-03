from django.contrib import admin
from django.urls import path
from apps.views import index, about, contact, home, new, blog, blog2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('home', home, name='homepage'),
    path('news', new, name='new'),
    path('blog', blog, name='blog'),
    path('', blog2, name='blog2'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
