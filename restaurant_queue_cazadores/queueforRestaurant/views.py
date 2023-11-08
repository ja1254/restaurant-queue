
from django.shortcuts import render, redirect
from .models import Reservation
from django.http import HttpResponse
from twilio.rest import Client
from django.db.models import Count

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

def estimate_time():

    peopleInQueue = Reservation.objects.annotate(numberOfPeople=Count("name")) # count the names in the reservation
    peopleCount = len(peopleInQueue) # get how many reservetions we have

    lstOfPeople = []

    for names in range(peopleCount):

        lstOfPeople.append(peopleInQueue[names].name) # make a list of the people in the queue exit
    #get the ammount of people in the queue
    #if there is one table waiting for 4 or less set it for 25 min wait
    # increment by 10 minutes each table of 4 or less
    # if the table is 5  then 45 minutes is the wait if busy 
    # if all tables are taken and there is a party of like 6+ then the wait is 1 hour maybe less
    

if __name__ == "__main__":
    estimate_time()



