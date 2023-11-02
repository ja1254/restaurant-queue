from django.urls import path
from . import views


app_name = 'queueforRestaurant'


urlpatterns = [
    path('', views.index, name='index'),  # <-- This is the new URL pattern for the homepage
    path('add/', views.add_to_queue, name='add_to_queue'),
]
