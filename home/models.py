from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Country=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    #Destination= models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Details(models.Model):
    name=models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    quantity=models.IntegerField()
    country=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    Dcountry = models.CharField(max_length=122)
    Dcity=models.CharField(max_length=122)

    def __str__(self):
        return self.name




