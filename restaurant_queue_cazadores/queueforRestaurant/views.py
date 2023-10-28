from django.shortcuts import render, redirect
from .models import Reservation

def add_to_queue(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        numberOfPeople = request.POST.get('numberOfPeople')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        
        reservation = Reservation(name=name, numberOfPeople=numberOfPeople, phoneNumber=phoneNumber, email=email)
        reservation.save()

        return redirect('') # develop a page that gives a confirmation
    return render(request, 'queueforRestaurant/add.html') #add.html is a template needs to be developed


def home(request):
    return render(request, 'home.html')

# Create your views here.

