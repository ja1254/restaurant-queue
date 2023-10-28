from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # <-- This is the new URL pattern for the homepage
    path('add/', views.add_to_queue, name = 'add_to_queue'),
]