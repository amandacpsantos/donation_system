from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from .views import new_item, update_item, delete_item, list_item, dashboard


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new/', new_item, name='new_item'),
    path('update/<int:id>', update_item, name='update_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('list/', list_item, name='list_item'),
]