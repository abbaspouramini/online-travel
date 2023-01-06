from django.contrib.auth.models import User
from django.db import models

class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userpassenger', null=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    bith_date = models.DateField()
    Gender_Choices = [('Male', 'Male'),('Female', 'Female')]
    gender= models.CharField(max_length=6,choices=Gender_Choices,default='Male')
    national_code = models.CharField(max_length=10)
