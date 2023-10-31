from django.shortcuts import render, redirect
from .models import Reservation
from django.http import HttpResponse

def index(request):
    return render(request, 'queueforRestaurant/index.html')

def add_to_queue(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        numberOfPeople = request.POST.get('numberOfPeople')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        
        reservation = Reservation(name=name, numberOfPeople=numberOfPeople, phoneNumber=phoneNumber, email=email)
        reservation.save()

        return redirect('') # develop a page that gives a confirmation
    return render(request, 'queueforRestaurant/add.html') 


# Create your views here.

