from email import message
from pyexpat import model
from unicodedata import category
from unittest.mock import Base
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactTable(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    name = models.CharField(max_length=200)
#    email = models.EmailField() 
#   subject = models.TextField()
#    message = models.TextField()

    def __str__(self) -> str:
        return self.email


class Category(models.Model):
    category = models.CharField(max_length=200)
    discrption = models.TextField()

    def __str__(self) -> str:
            return self.category   


class Dishes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pictures")
    desc = models.TextField()
    price = models.IntegerField(default=150)

    def __str__(self) -> str:
        return self.title   
    
class BookTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    numberofpeople = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

   
    
