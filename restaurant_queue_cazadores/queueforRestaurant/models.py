from django.db import models

# Create your models here.

# class Reservation that uses models to create the information we need
class Reservation(models.Model):

    name = models.CharField(max_length=100) 
    numberOfPeople = models.IntegerField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.name} at {self.time}"
    
    
 