from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from .views import new_item, update_item, delete_item, list_item, \
    dashboard, make_donation, list_donation, send_message, \
    historic_donation, check_donation, cancel_reservation_donation, cancel_donation


urlpatterns = [
    # ITEM
    path('', dashboard, name='dashboard'),
    path('new/', new_item, name='new_item'),
    path('update/<int:id>', update_item, name='update_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('list_item/', list_item, name='list_item'),

    # DONATION
    path('make_donation/<int:id_item>', make_donation, name='make_donation'),
    path('list_donation/', list_donation, name='list_donation'),
    path('historic_donation/', historic_donation, name='historic_donation'),
    path('cancel_reservation_donation/<int:id_item><int:id_donation>', cancel_reservation_donation, name='cancel_reservation_donation'),
    path('cancel_donation/<int:id_item>', cancel_donation, name='cancel_donation'),

    path('check_donation/<int:id_item>', check_donation, name='check_donation'),

    path('send_message/<int:id_item><int:id_donation>', send_message, name='send_message' ),



    #TESTE
    #path('get_user/', get_user, name='get_user')

]