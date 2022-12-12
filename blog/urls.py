from django.urls import path
from django.conf import settings
from blog.views import index,blog,contact,services,about,login,register
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
	path('', index,name='index'),
    path('blog/',blog, name='blog'),
    path('contact/',contact, name='contact'),
    path('services/',services, name='services'),
    path('about/',about, name='about'),
    path('login/',login, name='login'),
    path('register/',register, name='register'),
    ] 
