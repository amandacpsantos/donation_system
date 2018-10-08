from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from .views import new_item, update_item, delete_item, list_item, \
    dashboard, load_category, make_donation, list_donation


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new/', new_item, name='new_item'),
    path('update/<int:id>', update_item, name='update_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('list_item/', list_item, name='list_item'),
    path('ajax/load-categories/', load_category, name='ajax_load_categories'),

    path('make_donation/<int:id_item>', make_donation, name='make_donation'),
    path('list_donation/', list_donation, name='list_donation'),

]