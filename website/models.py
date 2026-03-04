from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Property(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50)
    beds = models.IntegerField()
    baths = models.IntegerField()
    sqft = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
       
class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    

class register(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=128) 
 
 
            