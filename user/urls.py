from django.urls import path, include
from .views import new_user, update_user, delete_user, list_user, profile_user


urlpatterns = [

    path('logup/', new_user, name='new_user'),

    path('update/', update_user, name='update_user'),
    path('delete/', delete_user, name='delete_user'),
    path('profile/', profile_user, name='profile_user'),
    path('list/', list_user, name='list_user'),

]