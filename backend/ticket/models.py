from django.db import models

from django.contrib.auth.models import User

from passenger.models import Passenger

class Train(models.Model):
    total_capacity = models.IntegerField()

class Station(models.Model):
    name = models.CharField(null=True, max_length=100)

class Trip(models.Model):
    train = models.ForeignKey(Train, related_name="trip_train", null=True, on_delete=models.CASCADE)
    start_station = models.ForeignKey(Station, related_name="start_station" ,on_delete=models.CASCADE, null=True)
    end_station = models.ForeignKey(Station, related_name="end_station" ,on_delete=models.CASCADE, null=True)
    start_time_date = models.DateTimeField()
    end_time_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # remaining_capacity = models.IntegerField(default=-1)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usertickets', null=True)
    number = models.CharField(max_length=8,primary_key=True,null=False,default=0)
    trip = models.ForeignKey(Trip, related_name="tickets", null=True, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, related_name="passtick", null=True, on_delete=models.CASCADE)
    seat_number = models.CharField(null=True, max_length=8)

