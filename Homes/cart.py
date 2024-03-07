from pickle import TRUE
from django.db import models
from Homes.models import *


class Cart(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True, blank=True)
    desc = models.TextField()
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.IntegerField(default=150)
    