from django.contrib import admin
from django.urls import path
from apps.views import index, about, contact, home, news, blog, blog2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('', home, name='homepage'),
    path('news', news, name='news'),
    path('blog', blog, name='blog'),
    path('blog2', blog2, name='blog2'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
