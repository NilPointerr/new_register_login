from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (register_1,login_1,logout_1,home_1,
                 dashboard)

urlpatterns = [
    path('register',register_1,name='register'),
    path('',login_1,name='login'),
    path('logout',logout_1,name='logout'),
    path('home',home_1,name= 'home'),
    path('dashboard',dashboard,name="dashboard"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)