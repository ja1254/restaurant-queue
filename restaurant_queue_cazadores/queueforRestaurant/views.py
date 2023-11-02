from django.shortcuts import render, redirect
from .models import Reservation
from django.http import HttpResponse
from twilio.rest import Client

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
        send_msm(name, phoneNumber)

        
    return render(request, 'queueforRestaurant/add.html') 

def send_msm(name, phoneNumber):
    
    account_sid = 'AC99d6836ccec48699b2221cd80189b597'
    auth_token = '9ae25d8e55b739ad0f0fa6c5ca300869'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18556999598',
        body = f'Hello {name}, thank you for joining the waitlist',
        to = f'{phoneNumber}'
    )



