from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    flight_name = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100 , null=True)
    departure_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    card_number = models.CharField(max_length=16, null=True)
    expiration_date = models.CharField(max_length=7, null=True)
    cvv = models.CharField(max_length=3, null=True)