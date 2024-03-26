
from django.shortcuts import render, redirect
from .models import Reservation
from django.http import HttpResponse
from twilio.rest import Client
from django.db.models import Count
#from gettersAndSetters import User

#function index that request the render of index.html
def index(request):
    return render(request, 'queueforRestaurant/index.html')

#function to add person to the queue
def add_to_queue(request):
    #if condition to check if the user entered the info
    if request.method == 'POST':
        name = request.POST.get('name')
        numberOfPeople = request.POST.get('numberOfPeople')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        #create a reservation and save it
        reservation = Reservation(name=name, numberOfPeople=numberOfPeople, phoneNumber=phoneNumber, email=email)
        reservation.save()
        #send message to the phone number
        send_msm(name, phoneNumber)

    #render the add page    
    return render(request, 'queueforRestaurant/add.html') 

# function that uses twilio to send message to a phone number
def send_msm(name, phoneNumber):
    
    account_sid = 'AC99d6836ccec48699b2221cd80189b597'
    auth_token = '9ae25d8e55b739ad0f0fa6c5ca300869'

    #create a client
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+18556999598',
        body = f'Hello {name}, thank you for joining the waitlist',
        to = f'{phoneNumber}'
    )

def getPeople():

    peopleInQueue = Reservation.objects.annotate(numberOfPeople=Count("name")) # count the names in the reservation
    peopleCount = len(peopleInQueue) # get how many reservetions we have

    lstOfPeople = []

    for names in range(peopleCount):

        lstOfPeople.append(peopleInQueue[names].name) # make a list of the people in the queue 

    

if __name__ == "__main__":
    getPeople()



