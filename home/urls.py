
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from .views import index
from item import urls as item_urls

urlpatterns = [
   #path('', index, name='index'),
   #path('dashboard/', include(item_urls))
]
